#encoding "utf-8" 

KeyWord -> "должнось" | "пост" | "профессия" ;
Position -> KeyWord Word;
Root -> Position interp (Definition.Noun);