{"filter":false,"title":"store.py","tooltip":"/chap6_flask-SQLAlchemy/models/store.py","undoManager":{"mark":48,"position":48,"stack":[[{"start":{"row":0,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["from db import db","","class ItemModel(db.Model):","    __tablename__ = 'items'","    id = db.Column(db.Integer, primary_key = True)","    name = db.Column(db.String(80))","    price = db.Column(db.Float(precision = 2))","    ","    def __init__(self,name,price):","        self.name = name","        self.price = price","","    @classmethod","    def find_by_name(cls,name):","\t    return cls.query.filter_by(name=name).first()","","    def json(self):","        return {'name' : self.name, 'price': self.price}","","    def save_to_db(self):","        db.session.add(self)","        db.session.commit()","","    def delete_from_db(self):","        db.session.delete(self)","        db.session.commit()","        ",""],"id":1}],[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["m"],"id":2},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["e"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["t"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["I"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["S"],"id":3},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["t"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["r"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":26},"action":"remove","lines":["items"],"id":4},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["s"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["t"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["o"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["r"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["e"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":46},"action":"remove","lines":["    price = db.Column(db.Float(precision = 2))"],"id":5}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":26},"action":"remove","lines":["        self.price = price"],"id":6}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["\t"],"id":8}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["d"],"id":9},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["e"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":[" "],"id":10},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["j"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["s"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["n"],"id":11}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":11},"action":"insert","lines":["()"],"id":12}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["s"],"id":13},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["e"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["l"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["f"]}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":[":"],"id":14}],[{"start":{"row":11,"column":16},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["\t\t"]}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":["\t"],"id":16}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["\t"],"id":17},{"start":{"row":11,"column":16},"end":{"row":12,"column":0},"action":"remove","lines":["",""]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":[":"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"remove","lines":[")"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["f"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["l"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["e"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["s"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["("]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"remove","lines":["n"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"remove","lines":["o"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"remove","lines":["s"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"remove","lines":["j"]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":[" "],"id":18},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"remove","lines":["f"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"remove","lines":["e"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"remove","lines":["d"]},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":37},"end":{"row":17,"column":42},"action":"remove","lines":["price"],"id":19},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["i"]},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["t"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["e"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["m"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":50},"end":{"row":17,"column":55},"action":"remove","lines":["price"],"id":20},{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"insert","lines":["i"]},{"start":{"row":17,"column":51},"end":{"row":17,"column":52},"action":"insert","lines":["t"]},{"start":{"row":17,"column":52},"end":{"row":17,"column":53},"action":"insert","lines":["e"]},{"start":{"row":17,"column":53},"end":{"row":17,"column":54},"action":"insert","lines":["m"]},{"start":{"row":17,"column":54},"end":{"row":17,"column":55},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":35},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["i"],"id":22},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["t"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["e"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["m"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":[" "],"id":23},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":[" "],"id":24},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["d"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["b"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["."]}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["r"],"id":25},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["e"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["l"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":19},"action":"remove","lines":["rela"],"id":26},{"start":{"row":7,"column":15},"end":{"row":7,"column":27},"action":"insert","lines":["relationship"]}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":29},"action":"insert","lines":["()"],"id":27}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":30},"action":"insert","lines":["''"],"id":28}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["I"],"id":29},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["t"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["e"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["m"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["M"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["o"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["d"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["e"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["l"]}],[{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"insert","lines":["["],"id":30},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["]"]}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["i"],"id":31},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["t"]},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["e"]},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["m"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["."]},{"start":{"row":19,"column":51},"end":{"row":19,"column":52},"action":"insert","lines":["j"]},{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"insert","lines":["s"]},{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"insert","lines":["o"]},{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":55},"end":{"row":19,"column":57},"action":"insert","lines":["()"],"id":32}],[{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":[" "],"id":33},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"insert","lines":["f"]},{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"insert","lines":["o"]},{"start":{"row":19,"column":60},"end":{"row":19,"column":61},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":[" "],"id":34},{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":["i"]},{"start":{"row":19,"column":63},"end":{"row":19,"column":64},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":63},"end":{"row":19,"column":64},"action":"remove","lines":["n"],"id":35}],[{"start":{"row":19,"column":63},"end":{"row":19,"column":64},"action":"insert","lines":["t"],"id":36},{"start":{"row":19,"column":64},"end":{"row":19,"column":65},"action":"insert","lines":["e"]},{"start":{"row":19,"column":65},"end":{"row":19,"column":66},"action":"insert","lines":["m"]}],[{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"insert","lines":[" "],"id":37},{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["i"]},{"start":{"row":19,"column":68},"end":{"row":19,"column":69},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":69},"end":{"row":19,"column":70},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":19,"column":70},"end":{"row":19,"column":71},"action":"remove","lines":["]"],"id":39}],[{"start":{"row":19,"column":80},"end":{"row":19,"column":81},"action":"insert","lines":["]"],"id":40}],[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":[","],"id":41}],[{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":[" "],"id":42},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["l"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["a"]},{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":["z"]},{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["y"]}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":[" "],"id":43},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":[" "],"id":44}],[{"start":{"row":7,"column":48},"end":{"row":7,"column":50},"action":"insert","lines":["''"],"id":45}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["d"],"id":46},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["y"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["n"]},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":["a"]},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":["m"]},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"insert","lines":["i"]},{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"insert","lines":["c"]}],[{"start":{"row":19,"column":80},"end":{"row":19,"column":81},"action":"insert","lines":["."],"id":47},{"start":{"row":19,"column":81},"end":{"row":19,"column":82},"action":"insert","lines":["a"]},{"start":{"row":19,"column":82},"end":{"row":19,"column":83},"action":"insert","lines":["l"]},{"start":{"row":19,"column":83},"end":{"row":19,"column":84},"action":"insert","lines":["l"]}],[{"start":{"row":19,"column":84},"end":{"row":19,"column":86},"action":"insert","lines":["()"],"id":48}],[{"start":{"row":10,"column":27},"end":{"row":10,"column":32},"action":"remove","lines":["price"],"id":49},{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"remove","lines":[","]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":26},"end":{"row":10,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1544740654640,"hash":"62f04a316a945ee820af447bcfea6fcc20bfb817"}