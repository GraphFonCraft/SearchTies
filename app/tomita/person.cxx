#encoding "utf-8" 

Person -> 	Word<gram="имя",gnc-agr[1]> (Word<gram="отч",gnc-agr[1]>) (Word<gram="фам",gnc-agr[1]>) | 
			Word<gram="фам",gnc-agr[1]> (Word<gram="имя",gnc-agr[1]>) (Word<gram="отч",gnc-agr[1]>);
Root -> Person interp (Definition.Noun);