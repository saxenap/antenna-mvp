class GroupedDataRegex:
    
    def __init__(
        self, joiner = '|'
    ):
        self.concat_char = joiner
        
    def make(self, groupby):
        return groupby.apply(
            lambda t: self.concat_char.join([str(i) for i in t])
        ).astype(str)

class GroupedDataRegexDecorator:
    
    def __init__(
        self, regexer, param, prefix, suffix
    ):
        self.regexer = regexer
        self.param = param
        self.prefix = prefix
        self.suffix = suffix
        
    def getType(self):
        return self.param
    
    def make(self, groupby):
        return (
            self.prefix
            + self.regexer.make(groupby)
            + self.suffix
        )

