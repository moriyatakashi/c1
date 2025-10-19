//////////////
// util

function hex4(val)
{
	str = "";
	for (var i = 0; i < 4; i++)
	{
		str +=
		"0123456789ABCDEF".charAt((val >>> (12 - i * 4)) & 0xF);
	}
	return str;
}

function unsignedDec(val)
{
	return "" + (val & 0xFFFF);
}

function signedDec(val)
{
	return "" + sxt(val & 0xFFFF);
}

function ea(val1, val2)
{
	return (val1 + val2) & 0xFFFF;
}

// sign extent
function sxt(val)
{
	val &= 0xFFFF;
	return (val < 0x8000) ? val : val - 65536;
}

function zxt(val)
{
	return val &= 0xFFFF;
}

function charCodeToJis8(charcode)
{
	if (charcode >= 0 && charcode <= 0x7f)
		return charcode;
	if (charcode >= 0xff61 && charcode <= 0xff9f)
		return charcode - 0xff61 + 0xa1;
	return -1;
}

function jis8ToCharCode(jis8)
{
	if (jis8 >= 0 && jis8 <= 0x7f)
		return jis8;
	if (jis8 >= 0xa1 && jis8 <= 0xdf)
		return jis8 - 0xa1 + 0xff61;
	return -1;
}

//////////////
// assembler

function Bits64K()
{
	this.ar = new Array(65536 / 32);
	this.count = 0;
	
	this.initialize = function()
	{
		for (var i = 0; i < this.ar.length; i++)
			this.ar[i] = 0;
		this.count = 0;
	}
	
	this.set = function(addr)
	{
		var offset = addr >>> 5;
		var mask = 1 << (addr % 32);

		if (!(this.ar[offset] & mask))
		{
			this.ar[offset] |= mask;
			this.count++;
		}
	}
	
	this.clear = function(addr)
	{
		var offset = addr >>> 5;
		var mask = 1 << (addr % 32);

		if (this.ar[offset] & mask)
		{
			this.ar[offset] &= ~mask;
			this.count--;
		}
	}
	
	this.isSet = function(addr)
	{
		var offset = addr >>> 5;
		var mask = 1 << (addr % 32);

		return (this.ar[offset] & mask) ? true : false;
	}
	
	this.getCount = function()
	{
		return this.count;
	}
	
	this.initialize();
}

var breakPointData = new Bits64K();
var macroFlag = new Bits64K();

// アセンブル用命令テーブルの要素のクラス

function AITableItem(code, fnc)
{
	this.code = code;		// 命令コード
	this.fnc = fnc;		// アセンブル処理関数
	
	this.callFnc = function(parsedLine)
	{
		this.fnc(this.code, parsedLine);
	}
}

var aITable =
{
	"NOP"   : new AITableItem(0x00, alNone),
	"LD"    : new AITableItem(0x10, alRMR),
	"ST"    : new AITableItem(0x11, alRM),
	"LAD"   : new AITableItem(0x12, alRM),
	"ADDA"  : new AITableItem(0x20, alRMR),
	"SUBA"  : new AITableItem(0x21, alRMR),
	"ADDL"  : new AITableItem(0x22, alRMR),
	"SUBL"  : new AITableItem(0x23, alRMR),
	"AND"   : new AITableItem(0x30, alRMR),
	"OR"    : new AITableItem(0x31, alRMR),
	"XOR"   : new AITableItem(0x32, alRMR),
	"CPA"   : new AITableItem(0x40, alRMR),
	"CPL"   : new AITableItem(0x41, alRMR),
	"SLA"   : new AITableItem(0x50, alRM),
	"SRA"   : new AITableItem(0x51, alRM),
	"SLL"   : new AITableItem(0x52, alRM),
	"SRL"   : new AITableItem(0x53, alRM),
	"JMI"   : new AITableItem(0x61, alM),
	"JNZ"   : new AITableItem(0x62, alM),
	"JZE"   : new AITableItem(0x63, alM),
	"JUMP"  : new AITableItem(0x64, alM),
	"JPL"   : new AITableItem(0x65, alM),
	"JOV"   : new AITableItem(0x66, alM),
	"PUSH"  : new AITableItem(0x70, alM),
	"POP"   : new AITableItem(0x71, alR),
	"CALL"  : new AITableItem(0x80, alM),
	"RET"   : new AITableItem(0x81, alNone),
	"SVC"   : new AITableItem(0xF0, alM),
	"START" : new AITableItem(-1, alStart),
	"END"   : new AITableItem(-1, alEnd),
	"DS"    : new AITableItem(-1, alDS),
	"DC"    : new AITableItem(-1, alDC),
	"IN"    : new AITableItem(1, alInOut),
	"OUT"   : new AITableItem(2, alInOut),
	"RPUSH" : new AITableItem(-1, alRPush),
	"RPOP"  : new AITableItem(-1, alRPop)	
};

// ラベルテーブル

function LabelTableItem()
{
	this.value = -1;			// 値0～0xFFFF 負はundefined
	this.defLine = -1;			// 定義している行
	this.refAddr = new Array();		// 参照しているアドレス
	this.refLine = new Array();		// 参照している行
	this.multiDefined = false;
}

var globalLabelTable;		// 全プログラム共通

var localLabelTable;		// STARTとENDの間
var startLabel;		// START命令のラベル。START命令に未遭遇ならnull
var startLocation;		// START命令のデフォルトのロケーション
var startOperand;		// START命令のオペランドのラベル。
var startLine;

function defineLabel(label)
{
	defineLabelSub(localLabelTable, label, locationCounter, lineNumber);
}

function defineGlobalLabel(label, value, line)
{
	defineLabelSub(globalLabelTable, label, value, line)
}

function defineLabelSub(table, label, value, line)
{
	var item = findOrCreateLabelTableItem(table, label);
	if (item.value >= 0)
	{
		item.multiDefined = true;
		logError(line, "多重定義されています - " + label);
	}
	else 
	{
		item.value = value;
		item.defLine = line;
	}
	// 多重定義ラベルの最初の行のエラーと、参照行のエラーは、END命令処理で最後に作る。
}

function referLabel(label, location)
{
	referLabelSub(localLabelTable, label, location, lineNumber);
}

function referGlobalLabel(label, location, line)
{
	referLabelSub(globalLabelTable, label, location, line);
}

function referLabelSub(table, label, location, line)
{
	var item = findOrCreateLabelTableItem(table, label);
	item.refAddr.push(location);
	item.refLine.push(line);
}

function findOrCreateLabelTableItem(table, label)
{
	var item = table[label];
	if (!item)
	{
		item = new LabelTableItem();
		table[label] = item;
	}
	return item;
}

// パース

function nParsedLine(){
	pa=new ParsedLine();
	pa.endcol="";
	pa.isEmpty="";
	return pa;
}
function ParsedLine()
{
	this.label = "";
	this.inst = "";
	this.operands = new Array();
	this.endcol = -1;
	
	this.isEmpty = function()
	{
		if (this.label == "" && this.inst == "" && this.operands.length == 0)
			return true;
		else
			return false;
	}
}

// エラー
function ErrorItem(lineNumber, message)
{
	this.lineNumber = lineNumber;
	this.message = message;
}

var errorMessages;
var errorShown = -1;

var scriptAllowed = false;

// アセンブラ　１パスで処理する

var locationCounter;		// アセンブル中のロケーションカウンター
var lineNumber;			// アセンブル中の行番号
var addressTable;			// 行ごとに表示するアドレスのテーブル
var nonExecutableTable;	// 実行可能行か？
var objectcode;			// オブジェクトコード
var entryPoint;			// エントリポイントアドレス。最初のスタートまたは指定されたアドレス

function assemble(arrayLines, initialLocation, tabWidth, entryPointName)
{
	globalLabelTable = new Object();
	errorMessages = new Array();
	addressTable = new Array(arrayLines.length);
	nonExecutableTable = new Array(arrayLines.length);
	breakPointData.initialize();
	macroFlag.initialize();
	enableElement("button_clear_break", breakPointData.getCount());
	
	startLabel = null;
	startOperand = null;
	startLine = -1;
	
	errorShown = -1;
	
	objectcode = new Array(65536);
	for (var i = 0; i < objectcode; i++)
		objectcode[i] = 0;
	entryPoint = -1;

	locationCounter = initialLocation;

	var endColTable = new Array(arrayLines.length);

	for (var i = 0; i < arrayLines.length; i++)
	{
		arrayLines[i] = formatSourceLine(arrayLines[i], tabWidth);
		addressTable[i] = -1;
		nonExecutableTable[i] = false;
		
		lineNumber = i;
		var parsedLine = parseLine(arrayLines[i]);
		endColTable[i] = parsedLine.endcol;


		if (parsedLine.inst == "IN")
		{
			if (!defined(window.opera) && defined(document.all) && defined(window.XMLHttpRequest))
			{
				if (!scriptAllowed)
				{
					var str = prompt("IN命令が実行可能な環境になっているかの確認です。\r\nお手数ですが [OK] を押してください。入力欄は空でかまいません。","");
					if (str != null)
					{
						scriptAllowed = true;
					}
					else
					{
						alert("情報バーに「スクリプト化されたウィンドウ」云々が出ていたら、お手数ですが、許可してから、[アセンブル] ボタンを押しなおしてください。IN命令の動作にはこの許可が必要です。");
						return -1;
					}
				}
			}
			else
			{
				scriptAllowed = true;
			}
		}


		if (!parsedLine.isEmpty())
		{
			// ラベルのチェック
			if (parsedLine.label != "")
			{
				if (!isLabel(parsedLine.label))
				{
					logError(i, "ラベル欄が不正です - " + parsedLine.label);
					parsedLine.label = "";
				}
			}
			assembleOneLine(parsedLine);
		}
		
		if (locationCounter > 0x10000)
		{
			logError(i, "COMET II コンピュータのメモリに入りきりません。アセンブルを中止します");
			break;
		}
	}
	
	if (locationCounter <= 0x10000)
	{
		// 後処理
		if (startLabel != null)
		{
			logError(arrayLines.length - 1, "END命令がありません");
			processEnd();
		}
			
		resolveGlobalReferences(entryPointName);
	}

	var nErrors = errorMessages.length;
	errorMessages.sort(function(item1, item2) {return item1.lineNumber - item2.lineNumber;});	
	
		
	// エラーログを出力
	{
		var arErrors = new Array();
		for (var i = 0; i < errorMessages.length; i++)
		{
			var item = errorMessages[i];
			arErrors.push('<a href="#" class="asm_error">');
			arErrors.push((1 + item.lineNumber) + '行目');
			arErrors.push('</a>');
			arErrors.push(enCER(" " + item.message));
			arErrors.push('<br />');
		}
		top.conframe.document.getElementById("errorlog").innerHTML = arErrors.join("");
		installAsmErrorHandlers();
	}
		
	// 表示データを作る
	{
		var arOut = new Array();	
		for (var i = 0; i < arrayLines.length; i++)
		{
			arOut.push('<div ' +
			                'id="line_' + i + '" ' +
			                'style="position:absolute; ' + 
			                       'top:' + (i * lineHeight) + 'px; ' + 
			                       'left:0px; ' + 
			                       'width:' + (lineHeight * 100) + 'px; ' +
			                       'height:' + lineHeight + 'px; ' +
			                       'font-size: ' + (lineHeight - 1) + 'px;' +
			                       'overflow: hidden; ' +
			                       '">');  
			var lineAddr = addressTable[i];
			
			if (lineAddr >= 0 && !nonExecutableTable[i])
			{
				arOut.push('<span id="line_addr_' + hex4(lineAddr) + '">');
			}
				
			// アドレスを出力
			if (lineAddr >= 0 && !nonExecutableTable[i])
			{
				arOut.push('<a href="#" class="addr" id="addr_addr_' + hex4(lineAddr) + '">');
				arOut.push('<span style="color: #804000; " class="addr_mark" id="addr_mark_' + hex4(lineAddr) + '">　</span>');　
				arOut.push(hex4(lineAddr));
				arOut.push('</a>');
			}
			else if (lineAddr >= 0)
			{
				arOut.push("　" + hex4(lineAddr));
			}
			else
			{
				arOut.push("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			}
			
			// 空白を出力
			arOut.push("&nbsp;");
			
			// 行を出力
			{
				var str = arrayLines[i];
				var len = str.length;
				var n = endColTable[i];
				
				if (n >= 0 && n < len)
				{
					arOut.push(enCER(str.substring(0, n)));
					arOut.push('<span style="color:#008000">');
					arOut.push(enCER(str.substring(n)));
					arOut.push('</span>');
				}
				else
				{
					arOut.push(enCER(arrayLines[i]));
				}
			}
			
			if (lineAddr >= 0 && !nonExecutableTable[i])
				arOut.push('</span>');
			
			arOut.push("</div>");
		}
		top.progframe.document.getElementById("progblock").innerHTML = arOut.join("");
		installBreakPointHandlers();
	}
	if (entryPoint < 0)
	{
		alert("ソースプログラムがありません。");
		return -1;
	}
	
	return nErrors;
}

function assembleOneLine(parsedLine)
{
	if (parsedLine.inst == "")
	{
		logError(lineNumber, "命令がありません");
		return;
	}
	
	var aiTableItem = aITable[parsedLine.inst];
	if (!aiTableItem)
	{
		logError(lineNumber, "命令欄が不正です - " + parsedLine.inst);
		return;
	}

	if (parsedLine.inst == "START")
		aiTableItem.callFnc(parsedLine);
	else if (parsedLine.inst == "END")
		aiTableItem.callFnc(parsedLine);
	else
	{
		// start命令がまだならエラーを出してstartの処理をする
		if (startLabel == null)
		{
			logError(lineNumber, "STARTがありません");
			processStart("", "");
		}
		
		// ラベルがあれば定義する
		if (parsedLine.label != "")
			defineLabel(parsedLine.label);
		
		// コード生成
		aiTableItem.callFnc(parsedLine);
	}	
}

function alStart(code, parsedLine)
{
	if (startLabel != null)
	{
		// すでにSTARTされている
		// ENDしてしまう
		logError(lineNumber, "END命令がありません");
		processEnd();
	}
	
	var label = "";
	var operand = "";
	
	if (parsedLine.label == "")
	{
		logError(lineNumber, "START命令にはラベルが必要です");
		label = "";
	}
	else if (isLabel(parsedLine.label))
		label = parsedLine.label;
	
	if (parsedLine.operands.length >= 1)
	{
		if (isLabel(parsedLine.operands[0]))
			operand = parsedLine.operands[0];
		else
			logError(lineNumber, "オペランドが不正です - " + parsedLine.operands[0]);

		if (parsedLine.operands.length > 1)
			logError(lineNumber, "余計なオペランドがあります");
	}
	processStart(label, operand);
}

function processStart(label, operand)
{
	startLabel = label;
	startLocation = locationCounter;
	startOperand = operand;
	startLine = lineNumber;
	nonExecutableTable[lineNumber] = true;
	
	// ローカルラベルテーブルをアサインする
	localLabelTable = new Object();
	
}

function alEnd(code, parsedLine)
{
	if (startLabel == null)
	{
		logError(lineNumber, "END命令が余計です");
		return;
	}

	if (parsedLine.label != "")
		logError(lineNumber, "END命令にはラベルはつけられません");

	if (parsedLine.operands.length != 0)
		logError(lineNumber, "余計なオペランドがあります");

//	addressTable[lineNumber] = locationCounter;
	
	processEnd();
}

function processEnd()
{
	// リテラルを展開
	for (var itemname in localLabelTable)
	{
		var item = localLabelTable[itemname];
		if (itemname.charAt(0) == '=')
		{
			// リテラルである。割り当てる
			defineLabel(itemname);
			allocConstant(itemname.substring(1));
		}
	}

	if (startLabel != "")	
	{
		// ローカル側にも一応登録する。参照しているかもしれないから。
		defineLabelSub(localLabelTable, startLabel, startLocation, startLine);
	
		// STARTのエントリポイントを求めてグローバル側に移す
		if (startOperand != "")
		{
			var item = localLabelTable[startOperand];
			if (item && item.value >= 0)
			{
				startLocation = item.value;
				localLabelTable[startLabel].value = item.value;
			}
			else // エラーである
				logError(startLine, "未定義です - " + startOperand);
		}
		
		addressTable[startLine] = startLocation;
		
		// グローバル側に定義する
		defineGlobalLabel(startLabel, startLocation, startLine);
		
		if (entryPoint < 0) // 最初のSTART文である。エントリポイントに登録する
			entryPoint = startLocation;
	}
	
	for (var itemname in localLabelTable)
	{
		var item = localLabelTable[itemname];
		// 未定義ラベルをグローバル側に統合
		if (item.value < 0)
			for (var i = 0; i < item.refAddr.length; i++)
				referGlobalLabel(itemname, item.refAddr[i], item.refLine[i]);
		// 多重定義ラベルにエラーを表示。定義箇所および参照箇所
		else if (item.multiDefined)
		{
			logError(item.defLine, "多重定義されています - " + itemname);
			for (var i = 0; i < item.refLine.length; i++)
				logError(item.refLine[i], "多重定義ラベルを参照しています - " + itemname);
		}
		// ローカル側の参照を解決
		else
			for (var i = 0; i < item.refAddr.length; i++)
				objectcode[item.refAddr[i]] = item.value;
	}


	startLabel = null;
	startOperand = null;
	startLine = -1;
		
}

function resolveGlobalReferences(entryPointName)
{
	for (var itemname in globalLabelTable)
	{
		var item = globalLabelTable[itemname];
		// 未定義ラベルをエラーにする
		if (item.value < 0)
			for (var i = 0; i < item.refLine.length; i++)
				logError(item.refLine[i], "未定義です - " + itemname);
		// 多重定義ラベル
		else if (item.multiDefined)
		{
			logError(item.defLine, "多重定義されています - " + itemname);
			for (var i = 0; i < item.refLine.length; i++)
				logError(item.refLine[i], "多重定義ラベルを参照しています - " + itemname);
		}
		// 参照を解決
		else
			for (var i = 0; i < item.refAddr.length; i++)
				objectcode[item.refAddr[i]] = item.value;
	}
	
	if (entryPointName != "")
	{
		var item = globalLabelTable[entryPointName.toUpperCase()];
		if ((!item) || item.value < 0)
			alert("実行開始ラベル欄で指定された" + entryPointName + "がプログラム中に存在しません");

		if (item)
			entryPoint = item.value;
	}		
}

function alNone(code, parsedLine)
{
	if (parsedLine.operands.length != 0)
		logError(lineNumber, "余計なオペランドがあります");

	addressTable[lineNumber] = locationCounter;
	objectcode[locationCounter++] = code << 8;
}

function alRM(code, parsedLine)
{
	alRMR2(code, parsedLine, false);
}

function alRMR(code, parsedLine)
{
	alRMR2(code, parsedLine, true);
}

function alRMR2(code, parsedLine, rrOK)
{
	var gr = 0;
	var addr = 0;
	var xr = 0;
	if (parsedLine.operands.length < 2)
		logError(lineNumber, "オペランドの数が不足です");
	else
	{
		gr = getGRCheck(parsedLine.operands[0]);
		if (rrOK)
		{
			gr2 = getGR(parsedLine.operands[1]);
			if (gr2 >= 0)
			{
				// RR命令である
				addressTable[lineNumber] = locationCounter;
				objectcode[locationCounter++] = (code | 0x04) << 8 | gr << 4 | gr2;
				return;
			}
		}
		addr = getAddrCheck(parsedLine.operands[1]);
		xr = getXRCheck(parsedLine.operands, 2);
	}
	addressTable[lineNumber] = locationCounter;
	objectcode[locationCounter++] = code << 8 | gr << 4 | xr;
	objectcode[locationCounter++] = addr;
}

function alM(code, parsedLine)
{
	var addr = 0;
	var xr = 0;
	
	if (parsedLine.operands.length < 1)
		logError(lineNumber, "オペランドの数が不足です");
	else
	{
		addr = getAddrCheck(parsedLine.operands[0]);
		xr = getXRCheck(parsedLine.operands, 1);
	}
	addressTable[lineNumber] = locationCounter;
	objectcode[locationCounter++] = code << 8 | xr;
	objectcode[locationCounter++] = addr;
}

function alR(code, parsedLine)
{
	var gr = 0;
	if (parsedLine.operands.length < 1)
		logError(lineNumber, "オペランドの数が不足です");
	else
	{
		gr = getGRCheck(parsedLine.operands[0]);
		if (parsedLine.operands.length > 1)
			logError(lineNumber, "余計なオペランドがあります");

	}
	addressTable[lineNumber] = locationCounter;
	objectcode[locationCounter++] = code << 8 | gr << 4;
}

function alDS(code, parsedLine)
{
	var count = 0;
	if (parsedLine.operands.length != 1)
		logError(lineNumber, "オペランドの数が不正です");
	else
	{
		var str = parsedLine.operands[0];
		if (str.match(/^[0-9]+$/))
			count = str - 0;
		else 
			logError(lineNumber, "オペランドが不正です - " + str);
	}
	addressTable[lineNumber] = locationCounter;
	nonExecutableTable[lineNumber] = true;
	locationCounter += count;
}

function alDC(code, parsedLine)
{
	if (parsedLine.operands.length == 0)
		logError(lineNumber, "オペランドがありません");
	else
	{
		addressTable[lineNumber] = locationCounter;
		nonExecutableTable[lineNumber] = true;
		
		for (var i = 0; i < parsedLine.operands.length; i++)
		{
			var str = parsedLine.operands[i];
			if (str.length == 0)
				logError(lineNumber, "オペランドが不正です");
			else
				if (!allocConstant(str))
					logError(lineNumber, "オペランドが不正です - " + str);
		}
	}
}

function allocConstant(str)
{
	var val = 0;
	if (isLabel(str))
		referLabel(str, locationCounter);
	else 
	{
		val = getDec(str);
		if (val < 0)
			val = getHex(str);
	}
	
	if (val >= 0)
	{
		objectcode[locationCounter++] = val;
		return true;
	}
	
	var ar = getStr(str);
	if (ar)
	{
		for (var j = 0; j < ar.length; j++)
			objectcode[locationCounter++] = ar[j];
		return true;
	}
	return false;
}

function alInOut(code, parsedLine)
{
	if (parsedLine.operands.length != 2)
	{
		logError(lineNumber, "オペランドの数が不正です");
		return;
	}

	addressTable[lineNumber] = locationCounter; 

	// PUSH 0,GR1
	objectcode[locationCounter++] = 0x7001;
	objectcode[locationCounter++] = 0x0000;
	// PUSH 0,GR2
	macroFlag.set(locationCounter);
	objectcode[locationCounter++] = 0x7002;
	objectcode[locationCounter++] = 0x0000;
	// LAD GR1,w1
	macroFlag.set(locationCounter);
	var addr1 = getAddrCheck(parsedLine.operands[0]);
	objectcode[locationCounter++] = 0x1210;
	objectcode[locationCounter++] = addr1;
	// LAD GR2,w2
	macroFlag.set(locationCounter);
	var addr2 = getAddrCheck(parsedLine.operands[1]);
	objectcode[locationCounter++] = 0x1220;
	objectcode[locationCounter++] = addr2;
	// SVC 1 or 2
	macroFlag.set(locationCounter);
	objectcode[locationCounter++] = 0xF000;
	objectcode[locationCounter++] = code;
	// POP GR2
	macroFlag.set(locationCounter);
	objectcode[locationCounter++] = 0x7120;
	// POP GR1
	macroFlag.set(locationCounter);
	objectcode[locationCounter++] = 0x7110;
}

function alRPush(code, parsedLine)
{
	if (parsedLine.operands.length != 0)
		logError(lineNumber, "余計なオペランドがあります");
	
	addressTable[lineNumber] = locationCounter;
	
	for (var i = 1; i <= 7; i++)
	{
		// PUSH 0,GRi
		if (i != 1)
			macroFlag.set(locationCounter);
		objectcode[locationCounter++] = 0x7000 + i;
		objectcode[locationCounter++] = 0x0000;
	}
}

function alRPop(code, parsedLine)
{
	if (parsedLine.operands.length != 0)
		logError(lineNumber, "余計なオペランドがあります");
	
	addressTable[lineNumber] = locationCounter;
	
	for (var i = 7; i >= 1; i--)
	{
		// POP GRi
		if (i != 7)
			macroFlag.set(locationCounter);
		objectcode[locationCounter++] = 0x7100 + (i << 4);
	}

}

// トークン解析

function isSpace(ch)
{
	if (ch <= ' ')
		return true;
	else
		return false;
}

function Token()
{
	this.indexNext = 0;
	this.token = "";
	
	this.getToken = function(str)
	{
		var n = this.indexNext;
		
		if (n >= str.length)
			return false;
	
		var ch = str.charAt(n);
		if (ch == ';')
			return false;
			
		if (ch == ',')
		{
			this.token = ",";
			this.indexNext = n + 1;
			return true;
		}
	
		if (isSpace(ch))
		{
			n++;
			while (n < str.length)
			{
				var ch = str.charAt(n);
				if (!isSpace(ch))
					break;
				n++;
			}
			this.token = " ";
			this.indexNext = n;			
			return true;
		}
		
		// スペースまたは,または;で区切られる
		var start = n;
		var inQuote = false;
		var ar = new Array;
		while (n < str.length)
		{
			var ch = str.charAt(n);
			if (inQuote)
			{
				if (ch == '\'')
					inQuote = false;
				ar.push(ch);
			}
			else
			{
				if (ch == '\'')
					inQuote = true;
				else if (isSpace(ch))
					break;
				else if (ch == ';')
					break;
				else if (ch == ',')
					break;
					
				ar.push(ch.toUpperCase());
			}
			n++;
		}	
		this.token = ar.join("");
		this.indexNext = n;
		return true;
	}
}

function isLabel(str)
{
	if (str.match(/^[A-Z][A-Z0-9]{0,7}$/))
		if (getGR(str) < 0)		// GRxはラベルには使えない
	    		return true;

	return false;
}

function parseLine(str)
{
	var parsedLine = new ParsedLine;

	var token = new Token;
	if (!token.getToken(str))
	{
		parsedLine.endcol = token.indexNext;
		return parsedLine;
	}
	
	// ラベルがあればラベルを取得	
	if (token.token != " ")
	{
		// ラベルつきである
		var label = token.token;
		parsedLine.label = label
		
		if (!token.getToken(str))
		{
			parsedLine.endcol = token.indexNext;
			return parsedLine;
		}
	}
	
	if (token.token != " ")
	{
		logError(lineNumber, "文法エラーです - " + token.token);
		return parsedLine;
	}
	
	// 命令を取得
	if (!token.getToken(str))
	{
		parsedLine.endcol = token.indexNext;
		return parsedLine;
	}
	
	parsedLine.inst = token.token;
	
	// 命令の後ろのスペースを取得
	if (!token.getToken(str))
	{
		parsedLine.endcol = token.indexNext;
		return parsedLine;
	}
		
	if (token.token != " ")
	{
		logError(lineNumber, "文法エラーです - " + token.token);
		return parsedLine;
	}
	
	// 最初のオペランドを取得
	if (!token.getToken(str))
	{
		parsedLine.endcol = token.indexNext;
		return parsedLine;
	}
	parsedLine.operands.push(token.token);
	
	// ２番目以降のオペランド
	while (true)
	{
		// カンマがあれば取得
		if (!token.getToken(str))
		{
			parsedLine.endcol = token.indexNext;
			return parsedLine;
		}
		if (token.token == " ")
		{
			parsedLine.endcol = token.indexNext;
			return parsedLine;
		}
		if (token.token != ",")
		{
			logError(lineNumber, "文法エラーです - " + token.token);
			return parsedLine;
		}
			
		// オペランドを取得
		if (!token.getToken(str) ||
			token.token == " " || token.token == ",")
		{
			logError(lineNumber, "文法エラーです - ,");
			return parsedLine;
		}
		parsedLine.operands.push(token.token);
	}
}

function getGR(str)
{
	if (str.length == 3 && str.substring(0, 2) == "GR")
	{
		var ch = str.charAt(2);
		if (ch >= '0' && ch <= '7')
			return ch - 0;
	}
	return -1;
}

function getGRCheck(str)
{
	var gr = getGR(str);
	if (gr >= 0)
		return gr;
	
	logError(lineNumber, "GRの指定が不正です - " + str);
	return 0;
}

function getXRCheck(operands, n)
{
	var xr = 0;
	if (operands.length > n)
	{
		xr = getGR(operands[n]);
		if (xr <= 0)
		{
			logError(lineNumber, "指標レジスタの指定が不正です - " + operands[n]);
			xr = 0;
		}		
	}
	if (operands.length > n + 1)
		logError(lineNumber, "余計なオペランドがあります");

	return xr;
}

function getAddrCheck(str)
{
	if (str.length == 0)
	{
		logError(lineNumber, "ADDRの指定がありません");
		return 0;
	}


	if (isLabel(str))
	{
		// ラベル
		referLabel(str, locationCounter + 1);
		return 0;
	}
	if (str.charAt(0) == '=')
	{
		// リテラル
		if (str.length == 1)
		{
			logError(lineNumber, "リテラル定数の指定がありません");
			return 0;
		}
		var str1 = str.substring(1);
		if (getDec(str1) >= 0 ||
		    getHex(str1) >= 0 ||
		    getStr(str1) != null)
		{
			// 正規のリテラルである。
			referLabel(str, locationCounter + 1);
			return 0;
		}
		
		// エラー
		logError(lineNumber, "リテラルの指定が不正です - " + str);
		return 0;
	}
	var val = getDec(str);
	if (val >= 0)
		return val;

	val = getHex(str);
	if (val >= 0)
		return val;

	// エラー	
	logError(lineNumber, "オペランドの指定が不正です - " + str);
	return 0;
}

function getDec(str)
{
	if (str.match(/^[+-]?[0-9]+$/))
		return (str - 0) & 0xFFFF;
		
	return -1;
}

function getHex(str)
{
	if (str.match(/^#[0-9A-Fa-f]+$/))
		return parseInt(str.substring(1), 16) & 0xFFFF;

	return -1;
}

function getStr(str)
{
	if (str.length < 2)
		return null;
	if (str.charAt(0) != '\'')
		return null;
		
	if (str.charAt(str.length - 1) != '\'')
		return null;
		
	var arCharCode = new Array();
		
	for (var i = 1; i < str.length - 1; i++)
	{
		ch = str.charAt(i);
		if (ch == '\'')
		{
			if (i < str.length - 1 && str.charAt(i + 1) == '\'')
			{
				arCharCode.push(ch.charCodeAt(0));
				i++;
			}
			else
				return null;
		}
		else
		{
			var jis8 = charCodeToJis8(str.charCodeAt(i));
			if (jis8 >= 0)
				arCharCode.push(jis8);
			else
				arCharCode.push("?".charCodeAt(0));
		}
	}
	return arCharCode;
}

function logError(lineNumber, message)
{
	errorMessages.push(new ErrorItem(lineNumber, message));
}

function installAsmErrorHandlers()
{
	var ar = top.conframe.document.getElementsByTagName("a");
	if (ar)
	{
		for (var i = 0; i < ar.length; i++)
		{
			var elem = ar[i];
			if (elem.className == "asm_error")
			{
				addEvent(elem, "click", onClickedError);
			}
		}
	}
	
}

function onClickedError(e)
{
	var elem = getEventTarget(e);
	if (elem)
	{
		var str = elem.innerHTML.match(/[0-9]+/);
		if (str)
		{
			var line = str - 1;
			
			if (errorShown >= 0)
			{
				var e = top.progframe.document.getElementById("line_" + errorShown);
				if (e)
					e.style.backgroundColor = "#FFFFFF";
			}
				
			e = top.progframe.document.getElementById("line_" + line);
			if (e)
			{
				e.style.backgroundColor = "#FFC0C0";
				errorShown = line;
			}	
		}
		scrollProgToShowLine(line);
	}
	preventDefault(e);
	return false;
}

function installBreakPointHandlers()
{
	var ar = top.progframe.document.getElementsByTagName("a");
	if (ar)
	{
		for (var i = 0; i < ar.length; i++)
		{
			var elem = ar[i];
			if (elem.className == "addr")
			{
				addEvent(elem, "click", onClickedBreakPoint);
			}
		}
	}
}

function onClickedBreakPoint(e)
{
	var elem = getEventTarget(e);
	if (elem)
	{
		var elem2 = top.progframe.document.getElementById("addr_mark_" + elem.id.substring(10));
		var addr = parseInt(elem.id.substring(10), 16);
		var str = elem2.innerHTML;
		if (str == "　")
		{
			elem2.innerHTML = "●";
			breakPointData.set(addr);
		}
		else
		{
			elem2.innerHTML = "　";
			breakPointData.clear(addr);
		}
	}
	enableElement("button_clear_break", breakPointData.getCount());
	
	
	preventDefault(e);
	return false;
}

function clearAllBreakPoints()
{
	var ar = top.progframe.document.getElementsByTagName("span");
	if (ar)
	{
		for (var i = 0; i < ar.length; i++)
		{
			var elem = ar[i];
			if (elem.className == "addr_mark")
			{
				elem.innerHTML = "　";
			}
		}
	}
	breakPointData.initialize();
	enableElement("button_clear_break", breakPointData.getCount());
}


//////////////
// exec

// 状態管理
var v = 0;
var STATE_NONE = v++;        // 未アセンブル状態　アセンブルエラー状態
var STATE_UNSTARTED = v++;   // 未起動状態
var STATE_BREAK = v++;       // ブレーク状態
var STATE_RUNNING = v++;     // 実行状態

var stateCurrent = STATE_NONE;

function setState(state)
{
	// 実行ボタンの操作
	enableButton("go", state == STATE_UNSTARTED || state == STATE_BREAK);
	enableButton("pause", state == STATE_RUNNING);
	enableButton("stepin", state == STATE_UNSTARTED || state == STATE_BREAK);
	enableButton("stepover", state == STATE_BREAK);
	enableButton("stepout", state == STATE_BREAK);
	enableElement("button_stop", state == STATE_BREAK || state == STATE_RUNNING);
	
	// ポーズ状態以外ではレジスタ、メモリの入力を抑制する
	var r = !(state == STATE_BREAK);
	for (var i = 0; i < 8; i++)
		setReadOnly("GR" + i, r);
	setReadOnly("PR", r);
	setReadOnly("SP", r);
	setReadOnly("ZF", r);
	setReadOnly("SF", r);
	setReadOnly("OF", r);
	for (var i = 0; i < 16; i++)
		setReadOnly("mem_" + i, r);
		
	// コンソール/エラーを切り替える
	var console = top.conframe.document.getElementById("console");
	var errorlog = top.conframe.document.getElementById("errorlog");
	
	console.style.position = (state == STATE_NONE) ? "absolute" : "relative";
	console.style.visibility = (state == STATE_NONE) ? "hidden" : "visible";
	errorlog.style.position = (state == STATE_NONE) ? "relative" : "absolute";
	errorlog.style.visibility = (state == STATE_NONE) ? "visible" : "hidden";
	
	stateCurrent = state;
}

function enableButton(id, enable)
{
	// ボタンのイネーブル、ディセーブル
	enableElement("button_" + id, enable);
	
	// ボタンイメージの取り替え
	var image = document.getElementById("buttonimage_" + id);
	var src = "images/" + (enable ? id : id + "_disabled") + ".gif";
	if (image.src != src)
		image.src = src;
}

function enableElement(id, enable)
{
	var elem = document.getElementById(id);
	var disabled = enable ? "" : "disabled";
	if (elem.disabled != disabled)
		elem.disabled = disabled;
}

function setReadOnly(id, readonly)
{
	var elem = document.getElementById(id);
	var readOnly = readonly ? "readonly" : "";
	if (elem.readOnly != readOnly)
		elem.readOnly = readOnly;
}


// COMET II のレジスタとメモリ
var gr = new Array(8);
var sp;
var pr;
var zf = 0;
var sf = 0;
var of = 0;
var mem = new Array(65536);
var address = 0;
var radix = 0;

var markedAddress = -1;
var consoleView;

function initializeRegMem()
{
	for (var i = 0; i < 8; i++)
		gr[i] = 0;
	
	sp = spInit;
	
	pr = entryPoint;
	zf = sf = of = 0;
	
	for (var i = 0; i < 65536; i++)
		mem[i] = objectcode[i];	
		
	top.progframe.scrollTo(0, 0);
	
	consoleView = new ConsoleView();

	sp = ea(sp, -1);
	mem[sp] = spInit;
	outputRegMem();
}



function outputRegMem()
{
	outputReg();
	outputMem();
}

function outputReg()
{
	var fnc = getRadix(hex4, unsignedDec, signedDec);

	// レジスタを出力
	for (var i = 0; i < 8; i++)
		document.getElementById("GR" + i).value = fnc(gr[i]);

	document.getElementById("SP").value = fnc(sp);		
	document.getElementById("PR").value = fnc(pr);
	
	// フラグを出力
	document.getElementById("ZF").value = "" + zf;
	document.getElementById("SF").value = "" + sf;
	document.getElementById("OF").value = "" + of;
	markPR();
}

function outputMem()
{	
	address = parseInt(document.getElementById("address").value, 16);
	if (isNaN(address))
		address = 0;

	var fnc = getRadix(hex4, unsignedDec, signedDec);
	var addr = getAddress();
	
	for (var i = 0; i < 16; i += 4)
		document.getElementById("addr_" + i).innerHTML = hex4(ea(addr, i));
	
	for (var i = 0; i < 16; i++)
		document.getElementById("mem_" + i).value = fnc(mem[ea(addr, i)]);
}

function inputRegMem()
{
	inputReg();
	inputMem();
}

function inputReg()
{
	var fnc = getRadix(fromHex, fromDec, fromDec);
	
	// レジスタを取得
	for (var i = 0; i < 8; i++)
		gr[i] = fnc(document.getElementById("GR" + i).value);
		
	sp = fnc(document.getElementById("SP").value);
	pr = fnc(document.getElementById("PR").value);
	
	// フラグを取得
	zf = fromDec(document.getElementById("ZF").value) ? 1 : 0;
	sf = fromDec(document.getElementById("SF").value) ? 1 : 0;
	of = fromDec(document.getElementById("OF").value) ? 1 : 0;
	
}

function inputMem()
{
	var fnc = getRadix(fromHex, fromDec, fromDec);
	var addr = getAddress();
	
	for (var i = 0; i < 16; i++)
		mem[ea(addr, i)] = fnc(document.getElementById("mem_" + i).value);
}

function fromHex(str)
{
	var n = parseInt(str, 16);
	if (isNaN(n))
		n = 0;
	return n & 0xFFFF;
}

function fromDec(str)
{
	var n = parseInt(str, 10);
	if (isNaN(n))
		n = 0;
	return n & 0xFFFF;
}

function getRadix(hex, unsigned, signed)
{
	if (radix == 0)
		return hex;
	if (radix == 1)
		return unsigned;
	if (radix == 2)
		return signed;
}

function getAddress()
{
	return address;
}

function onClickRadix()
{
	inputRegMem();

	if (document.getElementById("radix_hex").checked)
		radix = 0;
	if (document.getElementById("radix_unsigned").checked)
		radix = 1;
	if (document.getElementById("radix_signed").checked)
		radix = 2;

	outputRegMem();
}

function onChangeAddress()
{
	inputMem();
	
	address = parseInt(document.getElementById("address").value, 16);
	if (isNaN(address))
		address = 0;

	outputMem();
}

function markPR()
{
	if (markedAddress >= 0)
	{
		var elem = top.progframe.document.getElementById("line_addr_" + hex4(markedAddress));
		if (elem)
		{
			var nodeParent = elem.parentNode;
			if (nodeParent.id.substring(0, 5) == "line_")
			{
				nodeParent.style.backgroundColor = "#FFFFFF";
			}
		}
	}		
	markedAddress = -1;
	var elem = top.progframe.document.getElementById("line_addr_" + hex4(pr));
	if (elem)
	{
		var nodeParent = elem.parentNode;
		if (nodeParent.id.substring(0, 5) == "line_")
		{
			nodeParent.style.backgroundColor = "#FFFF00";
			markedAddress = pr;
		
			scrollProgToShowLine(nodeParent.id.substring(5) - 0);
		}
	}
}

function scrollProgToShowLine(lineNumber)
{
	var linesInWindow = getClientHeight(top.progframe) / lineHeight;
	var lineTop = getScrollPosY(top.progframe) / lineHeight;
	
	if (lineNumber >= lineTop && lineNumber < lineTop + linesInWindow - 1)
	{
	}
	else
	{
		top.progframe.scrollTo(0, lineNumber * lineHeight);
	}
}

function ConsoleView()
{
	this.arrayLines = new Array();
	this.lines = 25;
	
	this.update = function()
	{
		var filler = new Array();		
		for (var i = this.arrayLines.length; i < this.lines; i++)
			filler.push("<br />");
		
		top.conframe.document.getElementById("consolediv").innerHTML = this.arrayLines.join("") + filler.join("");
	}

	this.outputOneLine = function(start, len)
	{
		var arrayChars = new Array();
		for (var i = 0; i < len; i++)
		{
			var charCode = jis8ToCharCode(mem[zxt(start + i)]);
			if (charCode >= 0)
			{
				if (charCode <= 0x20 || charCode == 0x7F)
					charCode = 0x20;
				arrayChars.push(String.fromCharCode(charCode));
			}
			else
				arrayChars.push('?');
		}
		var str = enCER(arrayChars.join(""));
		
		
		while (this.arrayLines.length >= this.lines)
			this.arrayLines.shift();
		
		this.arrayLines.push(str + '<br />');
		
		this.update();
	}
	
	this.outputLine = function(start, lenaddr)
	{
		var len = mem[lenaddr];
		
		for (var i = 0; i < len; i += 80)
		{
			this.outputOneLine(zxt(start + i), Math.min(len - i, 80));
		}
	}
	
	this.inputLine = function(start, lenaddr)
	{
		var str = prompt("IN命令の入力内容 （キャンセルでEOF）", "");
		if (str != null)
		{
			var len = str.length;
			if (len > 256)
				len = 256;
			for (var i = 0; i < len; i++)
			{
				var jis8 = charCodeToJis8(str.charCodeAt(i));
				mem[zxt(start + i)] = jis8 >= 0 ? jis8 : "?".charCodeAt(0);
			}
			mem[lenaddr] = len;
			this.outputLine(start, lenaddr);
		}
		else
		{
			mem[lenaddr] = 0xFFFF;
		}
	}
	
	this.update();
}

var breakOnRet = false;

function stepIn()
{
	if (stateCurrent == STATE_NONE)
		return;
	if (stateCurrent == STATE_UNSTARTED)
	{
		initializeRegMem();
		setState(STATE_BREAK);
		return;
	}
	breakOnRet = false;
	inputRegMem();
	singleStep();
	outputRegMem();
}

function stepOut()
{
	if (stateCurrent != STATE_BREAK)
		return;

	breakOnRet = true;		
	callNest = 0;
	inputRegMem();
	setState(STATE_RUNNING);
	cont();
}

function stepOver()
{
	if (stateCurrent != STATE_BREAK)
		return;
	
	inputRegMem();
	if ((mem[pr] & 0xFF00) == 0x8000)
	{
		// CALL命令である。
		callNest = -1;
		breakOnRet = true;
		setState(STATE_RUNNING);
		cont();
	}
	else
	{
		// CALL命令以外はstepInと同じ
		breakOnRet = false;
		singleStep();
		outputRegMem();
	}
}

function go()
{
	if (stateCurrent == STATE_NONE)
		return;
	if (stateCurrent == STATE_UNSTARTED)
	{
		initializeRegMem();
	}

	breakOnRet = false;
	inputRegMem();
	setState(STATE_RUNNING);
	cont();
}

function cont()
{
	for (var i = 0; i < 100 && stateCurrent == STATE_RUNNING; i++)
		singleStep();
		
	if (stateCurrent == STATE_RUNNING)
		setTimeout("cont();", 1);
	else
		outputRegMem();
}

function pause()
{
	if (stateCurrent == STATE_RUNNING)
		setState(STATE_BREAK);
}

function stop()
{
	if (stateCurrent == STATE_BREAK || stateCurrent == STATE_RUNNING)
	{
		setState(STATE_UNSTARTED);
		alert("実行を中止しました。");
	}
}

function singleStep()
{
	do {
		executeOneInstruction();
		if (stateCurrent == STATE_UNSTARTED)
			return;
	} while (macroFlag.isSet(pr));

	if (breakPointData.isSet(pr))
	{
		setState(STATE_BREAK);
		return;
	}
	
	if (breakOnRet && callNest < 0)
	{
		setState(STATE_BREAK);
		return;
	}
	
	
}

//////////////
// comet

var callNest = 0;

function INST(w)
{
	this.code = (w >>> 8) & 0xFF;
	this.gr = (w >>> 4) & 7;
	this.x = w & 7;
	this.length2 = false;
	this.newPR = -1;
	
	this.getEA = function()
	{
		this.length2 = true;
		var ea = mem[zxt(pr + 1)];
		if (this.x)
			ea += gr[this.x];
		return zxt(ea);
	}
}

function setFR(value)
{
	zf = (value & 0xFFFF) ? 0 : 1; 
	sf = (value & 0x8000) ? 1 : 0;
	of = 0;
}

function setFROSigned(value)
{
	zf = (value & 0xFFFF) ? 0 : 1; 
	sf = (value & 0x8000) ? 1 : 0;
	of = (value < -32768 || value > 32767) ? 1 : 0;
}

function setFROUnsigned(value)
{
	zf = (value & 0xFFFF) ? 0 : 1; 
	sf = (value & 0x8000) ? 1 : 0;
	of = (value < 0 || value > 65535) ? 1 : 0;
}

function setFRC(w1, w2)
{
	if (w1 > w2)
	{
		sf = 0;
		zf = 0;
	}
	else if (w1 == w2)
	{
		sf = 0;
		zf = 1;
	}
	else
	{
		sf = 1;
		zf = 0;
	}
	of = 0;
}

function InstTableItem(fnc, fncop2)
{
	this.fnc = fnc;
	this.fncop2 = fncop2;
};

var instTable;

{
	instTable = new Array(256);
	for (var i = 0; i < 256; i++)
	{
		instTable[i] = new InstTableItem(instInvalid, null);
	}
	
	instTable[0x00] = new InstTableItem(instNOP, null);
	instTable[0x10] = new InstTableItem(instLD, op2m);
	instTable[0x11] = new InstTableItem(instST, null);
	instTable[0x12] = new InstTableItem(instLAD, null);
	instTable[0x14] = new InstTableItem(instLD, op2r);
	instTable[0x20] = new InstTableItem(instADDA, op2m);
	instTable[0x21] = new InstTableItem(instSUBA, op2m);
	instTable[0x22] = new InstTableItem(instADDL, op2m);
	instTable[0x23] = new InstTableItem(instSUBL, op2m);
	instTable[0x24] = new InstTableItem(instADDA, op2r);
	instTable[0x25] = new InstTableItem(instSUBA, op2r);
	instTable[0x26] = new InstTableItem(instADDL, op2r);
	instTable[0x27] = new InstTableItem(instSUBL, op2r);
	instTable[0x30] = new InstTableItem(instAND, op2m);
	instTable[0x31] = new InstTableItem(instOR, op2m);
	instTable[0x32] = new InstTableItem(instXOR, op2m);
	instTable[0x34] = new InstTableItem(instAND, op2r);
	instTable[0x35] = new InstTableItem(instOR, op2r);
	instTable[0x36] = new InstTableItem(instXOR, op2r);
	instTable[0x40] = new InstTableItem(instCPA, op2m);
	instTable[0x41] = new InstTableItem(instCPL, op2m);
	instTable[0x44] = new InstTableItem(instCPA, op2r);
	instTable[0x45] = new InstTableItem(instCPL, op2r);
	instTable[0x50] = new InstTableItem(instSLA, null);
	instTable[0x51] = new InstTableItem(instSRA, null);
	instTable[0x52] = new InstTableItem(instSLL, null);
	instTable[0x53] = new InstTableItem(instSRL, null);
	instTable[0x61] = new InstTableItem(instJMI, null);
	instTable[0x62] = new InstTableItem(instJNZ, null);
	instTable[0x63] = new InstTableItem(instJZE, null);
	instTable[0x64] = new InstTableItem(instJUMP, null);
	instTable[0x65] = new InstTableItem(instJPL, null);
	instTable[0x66] = new InstTableItem(instJOV, null);
	instTable[0x70] = new InstTableItem(instPUSH, null);
	instTable[0x71] = new InstTableItem(instPOP, null);
	instTable[0x80] = new InstTableItem(instCALL, null);
	instTable[0x81] = new InstTableItem(instRET, null);
	instTable[0xF0] = new InstTableItem(instSVC, null);
}

function executeOneInstruction()
{
	var w = mem[pr];
	var inst = new INST(w);
	var item = instTable[inst.code];
	item.fnc(inst);
	if (inst.newPR == spInit)
	{
		alert("プログラムが終了しました。");
		setState(STATE_UNSTARTED);
	}
	else if (inst.newPR >= 0)
		pr = inst.newPR;
	else if (inst.length2)
		pr = zxt(pr + 2);
	else
		pr = zxt(pr + 1);
}

function op2r(inst)
{
	return gr[inst.x];
}

function op2m(inst)
{
	return mem[inst.getEA()];
}

function instInvalid(inst)
{
}

function instNOP(inst)
{
}

function instLD(inst)
{
	setFR(gr[inst.gr] = zxt(this.fncop2(inst)));
}

function instST(inst)
{
	mem[inst.getEA()] = zxt(gr[inst.gr]);
}
	
function instLAD(inst)
{
	gr[inst.gr] = inst.getEA();
}

function instADDA(inst)
{
	var r = sxt(gr[inst.gr]) + sxt(this.fncop2(inst));
	setFROSigned(r);
	gr[inst.gr] = zxt(r);
}

function instSUBA(inst)
{
	var r = sxt(gr[inst.gr]) - sxt(this.fncop2(inst));
	setFROSigned(r);
	gr[inst.gr] = zxt(r);
}

function instADDL(inst)
{
	var r = zxt(gr[inst.gr]) + zxt(this.fncop2(inst));
	setFROUnsigned(r);
	gr[inst.gr] = zxt(r);
}

function instSUBL(inst)
{
	var r = zxt(gr[inst.gr]) - zxt(this.fncop2(inst));
	setFROUnsigned(r);
	gr[inst.gr] = zxt(r);
}

function instAND(inst)
{
	setFR(gr[inst.gr] = zxt(gr[inst.gr] & this.fncop2(inst))); 
}

function instOR(inst)
{
	setFR(gr[inst.gr] = zxt(gr[inst.gr] | this.fncop2(inst)));
}

function instXOR(inst)
{
	setFR(gr[inst.gr] = zxt(gr[inst.gr] ^ this.fncop2(inst)));
}

function instCPA(inst)
{
	setFRC(sxt(gr[inst.gr]), sxt(this.fncop2(inst)));
	
}

function instCPL(inst)
{
	setFRC(zxt(gr[inst.gr]), zxt(this.fncop2(inst)));
}

function instSLA(inst)
{
	var bits = inst.getEA();
	if (bits == 0)
	{
		setFR(gr[inst.gr]);
		return;
	}
	
	var w = zxt(gr[inst.gr]);
	var sign = w & 0x8000;
	w <<= bits;
	setFR(gr[inst.gr] = sign | (w & 0x7FFF));
	of = (w & 0x8000) ? 1 : 0;
} 

function instSRA(inst)
{
	var bits = inst.getEA();
	if (bits == 0)
	{
		setFR(gr[inst.gr]);
		return;
	}
	
	var w = sxt(gr[inst.gr]);
	
	setFR(gr[inst.gr] = zxt(w >> bits));
	of = (w >> (bits - 1)) & 1;
}

function instSLL(inst)
{
	var bits = inst.getEA();
	if (bits == 0)
	{
		setFR(gr[inst.gr]);
		return;
	}
		
	var w = zxt(gr[inst.gr]);
	w <<= bits;
	setFR(gr[inst.gr] = zxt(w));
	of = (w & 0x10000) ? 1 : 0;
}

function instSRL(inst)
{
	var bits = inst.getEA();
	if (bits == 0)
	{
		setFR(gr[inst.gr]);
		return;
	}
		
	var w = zxt(gr[inst.gr]);
	
	setFR(gr[inst.gr] = zxt(w >>> bits));
	of = (w >>> (bits - 1)) & 1;
}

function instJMI(inst)
{
	if (sf)
		instJUMP(inst);
	else
		inst.length2 = true;
}

function instJNZ(inst)
{
	if (!zf)
		instJUMP(inst);
	else
		inst.length2 = true;
}

function instJZE(inst)
{
	if (zf)
		instJUMP(inst);
	else
		inst.length2 = true;
}

function instJUMP(inst)
{
	inst.newPR = inst.getEA();
}

function instJPL(inst)
{
	if ((!zf) && (!sf))
		instJUMP(inst);
	else
		inst.length2 = true;
}

function instJOV(inst)
{
	if (of)
		instJUMP(inst);
	else
		inst.length2 = true;
}

function instPUSH(inst)
{
	sp = zxt(sp - 1);
	mem[sp] = inst.getEA();
}

function instPOP(inst)
{
	gr[inst.gr] = zxt(mem[sp]);
	sp = zxt(sp + 1);
}

function instCALL(inst, fncop2)
{
	inst.newPR = inst.getEA();
	sp = zxt(sp - 1);
	mem[sp] = zxt(pr + 2);
	callNest++;
}

function instRET(inst)
{
	inst.newPR = mem[sp];
	sp = zxt(sp + 1);
	callNest--;
}

function instSVC(inst)
{
	var ea = inst.getEA();
	if (ea == 1)
	{
		consoleView.inputLine(zxt(gr[1]), zxt(gr[2]));
	}
	else if (ea == 2)
	{
		consoleView.outputLine(zxt(gr[1]), zxt(gr[2]));
	}
	else
	{
		setState(STATE_BREAK);
	}
}
