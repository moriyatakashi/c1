from ba import*
class Aa:
    def __init__(self,pa):
        pb=True
        self.aa=pa
        pb=pb and ba3(self.aa)
        pb=pb and ba4(self.aa)
        pb=pb and ba5(self.aa)
        self.ab=pb
import json
pa=json.loads(open("a.json").read())
for pc in pa:
    pb=Aa(pc)
    print(pb.aa,pb.ab)
