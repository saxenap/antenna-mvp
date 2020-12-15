class RulesRegexBuilder:
    
    def __init__(self, regexer):
        self.regexer = regexer
        self.decorators = []
        
    def appendDecorator(self, decorator):
        self.decorators.append(decorator)
        
    def build(self, rules):
        regexes = {}
        
        for decorator in self.decorators:
            
            type = rules['matching']
            
            regex = rules[rules['matching'] == decorator.getType()][['service_id','text_match']]
            
            piped_regex = self.regexer.make(regex.groupby('service_id')['text_match'])
            regex = decorator.decorate(piped_regex).to_dict()
            
            inv_map = {v: k for k, v in regex.items()}
            regexes = {**regexes, **inv_map}
            
        return regexes


class GroupedDataRegex:
    
    def __init__(self, joiner = '|'):
        self.concat_char = joiner
        
    def make(self, groupby):
        return groupby.apply(
            lambda t: self.concat_char.join([str(i) for i in t])
        ).astype(str)
    

class RegexDecorator:
    
    def __init__(self, param, prefix, suffix):
        self.param = param
        self.prefix = prefix
        self.suffix = suffix
        
    def getType(self):
        return self.param
    
    def decorate(self, regex):
        return (
            self.prefix
            + regex
            + self.suffix
        )

