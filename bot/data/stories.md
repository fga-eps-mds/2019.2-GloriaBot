## Story greet
* greet OR start
    - utter_greet0
* greet2
    - utter_greet1

## Story delegacia
* delegacia
    - utter_delegacia
## Story orientacao
* orientacao OR affirm
    - utter_orientacao
>check_orientacao
## Story agride_agredido
>check_orientacao
* quem_agride_quem_agredido_1
    - utter_agrideAgredidoINICIO
* affirm OR deny
    - utter_agrideAgredidoInicioResposta
>check_agride_agredido_respostaAfirm
## Story agride_agredido_respostaAfirm
>check_agride_agredido_respostaAfirm
* affirm
    - utter_agrideAgredidoRespostaAfirm
    - utter_agrideAgredidoQuemPodeSofrer
>check_duvida
## Story agride_agredido_respostaDeny
>check_agride_agredido_respostaAfirm
* deny
    - utter_did_that_help
## Story agrideAgredidoQuemPodeSofrerAfirm
>check_duvida
* duvida
    - utter_agrideAgredidoQuemPodeSofrerAfirm
## Story manifestacaoDaViolencia
>check_orientacao
* manifestacaoDaViolencia
    -utter_manifestacaoDaViolencia

## Story manifestacao_fisica
* violenciaFisica
    - utter_violenciaFisica
## Story manifestacao_emocional
* violenciaEmocinal
    - utter_violenciaEmocional
## Story manifestacao_sexual
* violenciaSexual
    - utter_violenciaSexual
## Story manifestacao_CicloViolencia
* cicloViolencia
    - utter_cicloViolencia
## Story planoProtecao
>check_orientacao
* planoProtecao
    - utter_planoProtecao
>check_planoProtecao
## Story planoProtecao_horaAtaqueAffirm
>check_planoProtecao
* affirm
    - utter_horaAtaqueAffirm
## Story planoProtecao_Deny
>check_planoProtecao
* deny
    -utter_planoProtecaoDeny
>check_planoProtecao_Deny
## Story planoProtecao_DepoisAtaqueAffirm
>check_planoProtecao_Deny
* affirm
    - utter_depoisAtaqueAffirm
## Story planoProtecao_depoisAtaqueDeny
>check_planoProtecao_Deny
* deny
    - utter_depoisAtaqueDeny
## Story mitosViolencia
>check_orientacao
* mitosViolencia
    - utter_mitosViolencia
>check_mitos
## Story mitoUm
>check_mitos
* m1
    - utter_m1
## Story mitoDois
>check_mitos
* m2
    - utter_m2
## Story mitoTres
>check_mitos
* m3
    - utter_m3
## Story mitoQuatro
>check_mitos
* m4
    - utter_m4
## Story mitoCinco
>check_mitos
* m5
    - utter_m5
## Story mitoSeis
>check_mitos
* m6
    - utter_m6
## Story mitoSete
>check_mitos
* m4_7_Afirm
    - utter_m4_7_Afirm
## Story mitoOito
>check_mitos
* m8
    - utter_m8
## Story mitoNove
>check_mitos
* m5_9_Afirm
    - utter_m5_9_Afirm
## Story mitoDez
>check_mitos
* m10
    - utter_m10
## Story Aguentam_Relacao_Violenta
* aguentamRelacaoViolenta
    - utter_aguentamRelacaoViolenta
## Story antecipar_sinais
* anteciparSinais
    - utter_anteciparSinais
## Story origem_violencia
* origemViolencia
    - utter_origemViolencia
>check_origemViolenciaSIM
## Story origem_violenciaAffirm
>check_origemViolenciaSIM
* affirm
    - utter_origemViolenciaSIM
## Story MedirGravidade
>check_orientacao
* medirGravidade
    - utter_medirGravidade
>check_MedirGravidade
## Story MedirAgressorRotina
>check_MedirGravidade
* affirm
    - utter_MedirAgressorRotina
>check_MedirAgressorRotina
## Story MedirAgressorRotinaMedio
>check_MedirAgressorRotina
* deny
    - utter_MedirAgressorRotinaMedio
>check_MedirAgressorRotinaMedio
## Story MedirAgressorRotinaAlto
>check_MedirAgressorRotina
* duvida
    - utter_MedirAgressorRotinaAlto
>check_MedirAgressorRotinaAlto
## Story MedirAgressorRotinaExtremo
>check_MedirAgressorRotina
* affirm
    - utter_MedirAgressorRotinaExtremo
>check_MedirAgressorRotinaExtremo
## Story medir_Gravidade
>check_orientacao
* medirGravidade
    - utter_medirGravidade
>check_medir
## Story medir_AgressorFaca
>check_medir
* agressorFacaAffirm
    - utter_agressorFaca
>check_agressorFaca
## Story medir_AgressorFacaAffirm
>check_agressorFaca
* affirm OR agressorFacaAffirm
    - utter_altoRisco
>check_agressorFacaresp
## Story medir_AgressorFacaExt
>check_agressorFaca
* agressorFacaAffirmExt
    - utter_riscoExtremo
>check_agressorFacaresp
## Story Medir_AgressorDeny
>check_agressorFaca
* deny
    - utter_medioRisco
>check_agressorFacaresp
## Story Medir_ameaça
>check_agressorFacaresp
    - utter_ameaça
>check_Medir_ameaça
## Story Medir_ameaçaDeny
>check_Medir_ameaça
* deny
    - utter_ameaçaMedio
## Story Medir_ameaçaAffirm
>check_Medir_ameaça
* affirm
    - utter_ameaçaAffirm
>check_Medir_ameaçaAffirm
## Story Medir_ameaçaAlto
>check_Medir_ameaçaAffirm
* deny
    - utter_ameaçaAlto
## Story Medir_ameaçaExtremo
>check_Medir_ameaçaAffirm
* affirm
    - utter_ameaçaExtremo
## Story Recurso
>check_agressorFacaresp
    - utter_Recurso
>check_recurso
## Story RecursoMedio
>check_recurso
* deny
    - utter_RecursoMedio
## Story RecursoAffirm
>check_recurso
* affirm
    - utter_RecursoAffirm
>check_recursoAffirm
## Story RecursoAlto
>check_recursoAffirm
* deny
    - utter_RecursoAlto
## Story RecursoExtremo
>check_recursoAffirm
* affirm
    - utter_RecursoExtremo
## Story AgressorFilhos
>check_agressorFacaresp
    - utter_agressorFilhos
>check_AgressorFilhos
## Story AgressorFilhosMedio
>check_AgressorFilhos
* deny
    - utter_agressorFilhosMedio
## Story AgressorFilhosAffirm
>check_AgressorFilhos
* affirm
    - utter_agressorFilhosAffirm
>check_AgressorFilhosAffirm
## Story AgressorFilhosAlto
>check_AgressorFilhosAffirm
* ameaçarFilhos
    - utter_agressorFilhosAlto
## Story AgressorFilhosExtremo
>check_AgressorFilhosAffirm
* baterFilhos
    - utter_agressorFilhosExtremo
## Story Deixar_Agressor
>check_agressorFacaresp
    - utter_deixarAgressor
>check_deixarAgressor
## Story Deixar_AgressorDeny
>check_deixarAgressor
* deny
    - utter_deixarAgressorMedio
## Story Deixar_AgressorAffirm
>check_deixarAgressor
* affirm
    - utter_deixarAgressorAffirm
>check_deixarAgressorAffirm
## Story Deixar_AgressorImportar
>check_deixarAgressorAffirm
    - utter_deixarAgressorImportar
>check_deixarAgressorImportar
## Story Deixar_AgressorExtremo
>check_deixarAgressorImportar
* affirm OR agressivo
    - utter_deixarAgressorExtremo
## Story Deixar_AgressorAlto
>check_deixarAgressorImportar
* deny OR implorar
    - utter_deixarAgressorAlto
## Story medir_AgressorDeny
>check_agressorFaca
* deny
    - utter_medioRisco
## Story medir_AgressorControlador
>check_medir
* affirm
    - utter_agressorControlador
>check_agressorControlador
## Story medir_AgressorControladorAffirm
>check_agressorControlador
* affirm OR agressoControladorAffirm
    - utter_altoRisco
## Story medir_AgressoControladorExt
>check_agressorControlador
* agressoControladorAffirmExt
    - utter_riscoExtremo
## Story medir_agressoControladorDeny
>check_agressorControlador
* deny
    - utter_medioRisco
## Story medir_AgressorPreso
>check_medir
* affirm OR agressorPresoAffirm
    - utter_agressorPreso
>check_agressorPreso
## Story_medir_AgressorPresoAffirm
>check_agressorPreso
* affirm OR agressorPresoAffirm
    - utter_altoRisco
## Story_medir_AgressorPresoAffirmExt
>check_agressorPreso
* agressorPresoAffirmExt
    - utter_riscoExtremo
## Story_medir_AgressorPresoAffirmDeny
>check_agressorPreso
* deny
    - utter_medioRisco
