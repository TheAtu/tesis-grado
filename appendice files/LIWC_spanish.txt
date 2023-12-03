# -*- coding: utf-8 -*-
'''
Created on Nov. 11, 2014

@author: chaos

Modified on Mar. 26, 2023
@author: osama
https://www.redalyc.org/pdf/2430/243020635010.pdf
'''
import argparse, codecs, os, sys

class liwc:

    def load_liwc_dict(self, liwcdic_file):
        file_content = codecs.open(liwcdic_file, "r", "utf-8").read()
        cate_text = file_content[file_content.find("%")+1:file_content[1:].find("%")].strip()
        for line in cate_text.split("\n"):
            self.liwc_cate_name_by_number[int(line.strip().split("\t")[0])] = line.strip().split("\t")[1]

        dict_text = file_content[file_content[1:].find("%")+2:].strip()
        for line in dict_text.split("\n"):
            self.liwc_cate_number_by_word[line.strip().split("\t")[0]] = set([int(item) for item in line.strip().split("\t")[1:]])

    def __init__(self, liwcdic_file="Spanish_LIWC2007_Dictionary.dic"):
        
        self.liwc_category_names = ["WC",'Funct', 'TotPron', 'PronPer', 'Yo', 'Nosotro', 'TuUtd', 'ElElla', 'Ellos', 'PronImp', 'Articulo', 'Verbos', 'VerbAux', 'Pasado', 'Present', 'Futuro', 'Adverb', 'Prepos', 'Conjunc', 'Negacio', 'Cuantif', 'Numeros', 'Maldec', 'verbYO', 'verbTU', 'verbNOS', 'verbosEL', 'verbELLOS', 'Subjuntiv', 'VosUtds', 'formal', 'informal', 'verbVos', 'Social', 'Familia', 'Amigos', 'Humanos', 'Afect', 'EmoPos', 'EmoNeg', 'Ansiedad', 'Enfado', 'Triste', 'MecCog', 'Insight', 'Causa', 'Discrep', 'Tentat', 'Certeza', 'Inhib', 'Incl', 'Excl', 'Percept', 'Ver', 'Oir', 'Sentir', 'Biolog', 'Cuerpo', 'Salud', 'Sexual', 'Ingerir', 'Relativ', 'Movim', 'Espacio', 'Tiempo', 'Trabajo', 'Logro', 'Placer', 'Hogar', 'Dinero', 'Relig', 'Muerte', 'Asentir', 'NoFluen', 'Relleno']
        self.liwc_cate_name_by_number = {}
        self.liwc_cate_number_by_word = {}

        if os.path.exists(liwcdic_file) == False:
            
            sys.exit()
        else:
            self.load_liwc_dict(liwcdic_file)

    def getLIWCCount(self, text):
        count_by_categories = {"WC":0,'Funct': 0, 'TotPron': 0, 'PronPer': 0, 'Yo': 0, 'Nosotro': 0, 'TuUtd': 0, 'ElElla': 0, 'Ellos': 0, 'PronImp': 0, 'Articulo': 0, 'Verbos': 0, 'VerbAux': 0, 'Pasado': 0, 'Present': 0, 'Futuro': 0, 'Adverb': 0, 'Prepos': 0, 'Conjunc': 0, 'Negacio': 0, 'Cuantif': 0, 'Numeros': 0, 'Maldec': 0, 'verbYO': 0, 'verbTU': 0, 'verbNOS': 0, 'verbosEL': 0, 'verbELLOS': 0, 'Subjuntiv': 0, 'VosUtds': 0, 'formal': 0, 'informal': 0, 'verbVos': 0, 'Social': 0, 'Familia': 0, 'Amigos': 0, 'Humanos': 0, 'Afect': 0, 'EmoPos': 0, 'EmoNeg': 0, 'Ansiedad': 0, 'Enfado': 0, 'Triste': 0, 'MecCog': 0, 'Insight': 0, 'Causa': 0, 'Discrep': 0, 'Tentat': 0, 'Certeza': 0, 'Inhib': 0, 'Incl': 0, 'Excl': 0, 'Percept': 0, 'Ver': 0, 'Oir': 0, 'Sentir': 0, 'Biolog': 0, 'Cuerpo': 0, 'Salud': 0, 'Sexual': 0, 'Ingerir': 0, 'Relativ': 0, 'Movim': 0, 'Espacio': 0, 'Tiempo': 0, 'Trabajo': 0, 'Logro': 0, 'Placer': 0, 'Hogar': 0, 'Dinero': 0, 'Relig': 0, 'Muerte': 0, 'Asentir': 0, 'NoFluen': 0, 'Relleno': 0}

        count_by_categories["WC"] = len(text.split())

        for word in text.split():

            cate_numbers_word_belongs = set([])
            if word in self.liwc_cate_number_by_word:
                cate_numbers_word_belongs = self.liwc_cate_number_by_word[word]

            else:

                #liwc words have *. eg: balcon*
                word = word[:-1]
                while len(word) > 0:
                    if (word+"*") in self.liwc_cate_number_by_word:
                        cate_numbers_word_belongs = self.liwc_cate_number_by_word[word+"*"]
                        break
                    else:
                        word = word[:-1]

            for num in cate_numbers_word_belongs:
                count_by_categories[self.liwc_cate_name_by_number[num]] += 1

        return count_by_categories


'''
if (__name__ == "__main__"):
    ################################################
    #set arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--liwcdic", action="store", dest="liwcdic", default="LIWC2007_English100131.dic", help="LIWC dic")
    parser.add_argument("--input", action="store", dest="input", default="input.txt", help="The input file")
    parser.add_argument("--output", action="store", dest="output", default="output.txt", help="The output file")

    args = parser.parse_args()
    liwcdic_file = args.liwcdic
    input_file = args.input
    output_file = args.output

    if output_file == "output.txt":
        output_file = input_file+".liwc_count.txt"

    ################################################
    liwc_counter = LIWC_Counter(liwcdic_file)

    fw = codecs.open(output_file, "w", "utf-8")
    
    fw.write(u"ID\t")
    fw.write(u"{0}\n".format(u"\t".join( liwc_counter.liwc_category_names )))

    
    for line in codecs.open(input_file, encoding="utf-8"):

        if line.find("\t") == -1:
            continue

        id = line[:line.find("\t")].strip()
        text = line[line.find("\t")+1:].strip()
        count_by_categories = liwc_counter.get_count_for_all_liwc_categories(text)

        fw.write(u"{0}".format(id))
        for cate in liwc_counter.liwc_category_names:
            fw.write(u"\t{0}".format(count_by_categories[cate]))
        fw.write(u"\n")
                    
    fw.close() 
            
'''        
        
        
text="Anoche vi un documental sobre una mujer el un ataúd de hierro. Sucedió que había una obra de construcción en Queens, Nueva York, y los trabajadores, usando el excavador, golpearon algo muy duro. Resultó que era un ataúd de hierro dentro del cual había una mujer negra que murió hace 150 años de viruela. Eso causó que los trabajadores llamaron al Centro para el Control de Enfermedades para averiguar si habría un riesgo sanitario para el público. Los científicos dedujeron que el ADN del virus había desintegrado tanto que no había peligro, así que la investigación seguía."
L=liwc().getLIWCCount(text)
#L2=liwc2007().getLIWCCount(text)    
    
    