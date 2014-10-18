#encoding "utf-8"    // сообщаем парсеру о том, в какой кодировке написана грамматика
#GRAMMAR_ROOT Def      // указываем корневой нетерминал грамматики

Addic -> LBracket AnyWord+ RBracket;
Linker -> Hyphen | Hyphen "это" | "являться" | "это" ;

Person -> 	Word<gram="имя"> (Word<gram="отч">) (Word<gram="фам">) | 
			Word<gram="фам"> (Word<gram="имя">) (Word<gram="отч">);
			
DefTarget -> Noun | Person;

Def -> 	DefTarget 
		(Addic) Linker 
		Noun<kwtype="словосочетания"> interp (Definition.Noun); 

