#encoding "utf-8" 
#GRAMMAR_ROOT Root      // указываем корневой нетерминал грамматики
#GRAMMAR_KWSET [bad_output]
Combo -> Word<GU=[A],gnc-agr[1]> interp (Definition.Adj) Noun<gnc-agr[1], rt>;
Root -> Combo interp (Definition.Noun);