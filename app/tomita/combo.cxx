#encoding "utf-8" 

Connector -> Comma | SimConjAnd | "или";
ComboSpree -> Combo | Combo<c-agr[1]> Connector Combo<c-agr[1]>;
AdjSpree -> Adj<gnc-agr[1]> Adj<gnc-agr[1]>* | 
	AdjSpree<gnc-agr[1]> Connector AdjSpree<gnc-agr[1]>;
Combo -> AdjSpree<gnc-agr[1]> Noun<gnc-agr[1], no_hom, rt>;
