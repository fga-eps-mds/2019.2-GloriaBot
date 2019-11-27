## Story greet
* greet OR start
    - utter_greet0
>check_greet
## Story greet
>check_greet
* greet2
    - utter_greet1
## Story delegacia
>check_greet
* delegacia
    - utter_delegacia
## Story orientacao
* orientacao OR affirm
    - utter_orientacao
>check_orientacao

## Story MedirGravidade
* medirGravidade
    - utter_medirGravidade
>check_medir
## Story medir OK
>check_medir
* affirm
    -utter_agressorFaca
>check_agressorFaca
## Agressor faca
>check_agressorFaca
* affirm OR faca
    - utter_facaAltoRisco
    - action_restart
## Agressor faca
>check_agressorFaca
* ameaca
    - utter_facaRiscoExtremo
## Agressor faca
>check_agressorFaca
* deny
    - utter_agressorPreso
>check_agressorPreso
## Story_medir_AgressorPresoAffirm
>check_agressorPreso
* affirm OR agressorPresoAffirm
    - utter_presoAltoRisco
## Story medir_AgressorControlador
>check_agressorPreso
* deny
    - utter_agressorControlador
>check_agressorControlador

## Story medir_AgressorControladorAffirm
>check_agressorControlador
* affirm OR agressoControladorAffirm
    - utter_controladorAltoRisco

## Story medir_AgressoControladorExt
>check_agressorControlador
* agressoControladorAffirmExt
    - utter_controladorRiscoExtremo

## Story medir_AgressoControladorExt
>check_agressorControlador
* deny
    - utter_agressorFilhos
>check_AgressorFilhos

## Story AgressorFilhosAffirm
>check_AgressorFilhos
* affirm
   - utter_agressorFilhosAffirm
>check_AgressorFilhosAffirm

## Story AgressorFilhosAlto
>check_AgressorFilhosAffirm
* ameaca
    - utter_agressorFilhosAlto
## Story AgressorFilhosExtremo
>check_AgressorFilhosAffirm
* baterFilhos
    - utter_agressorFilhosExtremo
    - utter_delegacia
## Story Caso o agressor tenha ameaçado a vítima
>check_AgressorFilhos
* deny
    -  utter_deixarAgressor
>check_deixarAgressor
## Story Deixar_AgressorAffirm
>check_deixarAgressor
* affirm
  - utter_deixarAgressorAffirm
>check_deixarAgressorAffirm

## Story Deixar_AgressorImportar
>check_deixarAgressorAffirm
* affirm
  - utter_deixarAgressorImportar
>check_deixarAgressorImportar

## Story Deixar_AgressorExtremo
>check_deixarAgressorImportar
* affirm OR baterFilhos
  - utter_deixarAgressorExtremo
## Story Deixar_AgressorAlto
>check_deixarAgressorImportar
* deny OR implorar
  - utter_deixarAgressorAlto
## Story Deixar_AgressorDeny
>check_deixarAgressor
* deny
  - utter_Recurso
>check_recurso
## Story RecursoAffirm
>check_recurso
* affirm
  - utter_RecursoAffirm
>check_recursoAffirm
## Story RecursoAlto
>check_recursoAffirm
* trabalho
  - utter_RecursoAlto
## Story RecursoExtremo
>check_recursoAffirm
* informacao
  - utter_RecursoExtremo

## Story RecursoAffirm
>check_recurso
* deny
    - utter_ameaca
>check_Medir_ameaca
## Story Medir_ameaçaAffirm
>check_Medir_ameaca
* affirm
  - utter_ameacaAffirm
>check_Medir_ameacaAffirm
## Story Medir_ameaçaAffirm
>check_Medir_ameaca
* deny
  - utter_MedirAgressorRotina
>check_MedirAgressorRotina
## Story MedirAgressorRotinaAlto
>check_MedirAgressorRotina
* duvida
    - utter_MedirAgressorRotinaAlto
## Story MedirAgressorRotinaExtremo
>check_MedirAgressorRotina
* affirm
    - utter_MedirAgressorRotinaExtremo
## Story forcarAtosSexuais
>check_MedirAgressorRotina
* deny
    - utter_forcarAtosSexuais
>check_forcarAtosSexuais
## Story forcarAtosAlto
>check_forcarAtosSexuais
* duvida
    - utter_forcarAtosAlto
## Story forcarAtosExtremo
>check_forcarAtosSexuais
* affirm
    - utter_forcarAtosExtremo
## Story bebidaDrogasMedio
>check_bebidaDrogas
* deny  
    - utter_suicida
>check_suicida
## Story suicidaAlto
>check_suicida
* duvida
    - utter_suicidaAlto
## Story suicidaExtremo
>check_suicida
* affirm
    - utter_suicidaExtremo
## Story suicidaMedio
>check_suicida
* deny
    - utter_maluco
>check_maluco
## Story malucoAlto
>check_maluco
* duvida
    - utter_malucoAlto
## Story malucoExtremo
>check_maluco
* affirm
    - utter_malucoExtremo

## Story forcarAtosMedio
>check_forcarAtosSexuais
* deny
    - utter_bebidaDrogas
>check_bebidaDrogas
## Story bebidaDrogasAlto
>check_bebidaDrogas
* duvida
    - utter_bebidaDrogasAlto
## Story bebidaDrogasExtremo
>check_bebidaDrogas
* affirm
    - utter_bebidaDrogasExtremo

## Story Medir_ameaçaAlto
>check_Medir_ameacaAffirm
* deny
  - utter_ameacaAlto
## Story Medir_ameaçaExtremo
>check_Medir_ameacaAffirm
* affirm
  - utter_ameacaExtremo

## Story Aguentam_Relacao_Violenta
* relacaoViolenta
    - utter_aguentamRelacaoViolenta
>check_relacaoViolenta
## Story Aguentam_Relacao_ViolentaDeny
>check_relacaoViolenta
* deny
    - utter_maisAlgumaCoisa
## Story riscoRomp
>check_relacaoViolenta
* rompimento
    - utter_riscoRomp
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story vergonhaMedo
>check_relacaoViolenta
* relacaoViolenta
    - utter_vergonhaMedo
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story esperanca
>check_relacaoViolenta
* esperanca
    - utter_esperanca
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story isolamento
>check_relacaoViolenta
* isolamento
    - utter_isolamento
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story negacao
>check_relacaoViolenta
* negacao
    - utter_negacao
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story barreiras
>check_relacaoViolenta
* barreiras
    - utter_barreiras
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story dependencia
>check_relacaoViolenta
* dependencia
    - utter_dependencia
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story deixarAgressor
>check_relacaoViolenta
* deixarAgressor
    - utter_deixarAgressor
    - utter_maisAlgumaCoisa
>check_relacaoResp
## Story relacaoRespAffirm
>check_relacaoResp
* affirm
    - utter_greet1
## Story relacaoRespDeny
>check_relacaoResp
* deny
    - utter_goodbye

## Story planoProtecao
>check_orientacao
* planoProtecao
    - utter_planoProtecao
>check_plano
## Story planoProtecaoDepois
>check_plano
* depoisAtaque
    - utter_depoisAtaque
    - utter_depoisAtaque2
    - utter_depoisAtaque3
    - utter_maisAlgumaCoisa
>check_loop
## Story planoProtecaoHora
>check_plano
* horaAtaque
    - utter_horaAtaque

## Story agride_agredido
* quem_agride_quem_agredido_1
    - utter_agrideAgredidoINICIO
* affirm OR deny
    - utter_agrideAgredidoInicioResposta
>check_agride_agredido_respostaAfirm
## Story agride_agredidoDeny
>check_agride_agredido_respostaAfirm
* deny
    - utter_maisAlgumaCoisa
## Story agride_agredido_respostaAfirm
>check_agride_agredido_respostaAfirm
* affirm
    - utter_agrideAgredidoRespostaAfirm
    - utter_agrideAgredidoQuemPodeSofrer
>check_duvida
## Story agride_agredido_respostaDeny
>check_agride_agredido_respostaAfirm
* deny
    - utter_maisAlgumaCoisa
>check_maisAlgumaCoisa
## Story agrideAgredidoQuemPodeSofrerAfirm
>check_duvida
* affirm
    - utter_agrideAgredidoQuemPodeSofrerAfirm
## Story goodbye
>check_maisAlgumaCoisa
* deny
    - utter_goodbye

## Story manifestacaoDaViolencia
>check_orientacao
* manifestacaoDaViolencia
    - utter_manifestacaoDaViolencia
>check_manifestacao
## Story manifestacaoDaViolenciaDeny
>check_manifestacao
* deny
    - utter_maisAlgumaCoisa
>check_loop
## Story manifestacao_fisica
>check_manifestacao
* violenciaFisica
    - utter_violenciaFisica
    - utter_maisAlgumaCoisa
>check_loop
## Story manifestacao_emocional
>check_manifestacao
* violenciaEmocional
    - utter_violenciaEmocional
    - utter_maisAlgumaCoisa
>check_loop
## Story manifestacao_sexual
>check_manifestacao
* violenciaSexual
    - utter_violenciaSexual
    - utter_maisAlgumaCoisa
>check_loop
## Story manifestacao_CicloViolencia
>check_manifestacao
* cicloViolencia
    - utter_cicloViolencia
    - utter_maisAlgumaCoisa
>check_loop

## Story origemViolencia
>check_orientacao
* origemViolencia
    - utter_origemViolencia
>check_origemViolencia
## Story origemViolenciaAffirm
>check_origemViolencia
* affirm
    - utter_origemViolenciaSIM
    - utter_origemViolencia2
    - utter_origemViolencia3
    - utter_maisAlgumaCoisa
>check_loop
## Story origemViolenciaDeny
>check_origemViolencia
* deny
    - utter_maisAlgumaCoisa
>check_loop

## Story_anteciparSinais
>check_orientacao
* anteciparSinais
    - utter_anteciparSinais
    - utter_maisAlgumaCoisa
>check_loop

## Story LoopDeny
>check_loop
* deny
    - utter_goodbye
## Story LoopAffirm
>check_loop
* affirm
    - utter_greet1
>check_loopResp
## Story Loopresp
>check_loopResp
* deny
    - utter_goodbye
