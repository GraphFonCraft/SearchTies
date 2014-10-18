#encoding "utf-8" 

Person -> 	Word<gram="имя"> (Word<gram="отч">) (Word<gram="фам">) | 
			Word<gram="фам"> (Word<gram="имя">) (Word<gram="отч">);
Root -> Person interp (Definition.Noun);