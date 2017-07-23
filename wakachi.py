from janome.tokenizer import Tokenizer

t = Tokenizer('dict.csv')

wakachilist = []

with open('all_ziburi_text.wkc', 'w', encoding = 'utf8') as f1:
    with open('all_ziburi_text.txt', 'r', encoding = 'utf8') as f2:
        for line in f2:
            wordlist = []
            tokens = t.tokenize(line.rstrip('\n'))
            for token in tokens:
                check = token.part_of_speech.split(',')
                if check[0] == '名詞':
                    wordlist.append(token.surface)
                elif check[0] != '記号':
                    wordlist.append(token.base_form)
            
            f1.writelines(' '.join(wordlist) + '\n')
        
    


