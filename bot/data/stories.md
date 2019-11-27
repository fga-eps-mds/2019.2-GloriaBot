## Story greet
* greet OR start
    - utter_greet0
* greet2
    - utter_greet1
## sroty greet1
* greet2
    - utter_greet1
## Story delegacia
* delegacia
    - utter_delegacia
## Story orientacao
* orientacao OR affirm
    - utter_orientacao
>check_orientacao

## Story MedirGravidade
>check_orientacao
* medirGravidade
    - utter_medirGravidade
>check_medir
## Story medir OK
>check_medir
* ok
    -utter_agressorFaca
>check_agressorFaca
## Agressor faca
>check_agressorFaca
* affirm OR faca
    - utter_facaAltoRisco
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
>check_orientacao
* aguentamRelacaoViolenta
    - utter_aguentamRelacaoViolenta
>check_relacaoViolenta
## Story riscoRomp
>check_relacaoViolenta
* rompimento
    - utter_riscoRomp
## Story vergonhaMedo
>check_relacaoViolenta
* relacaoViolenta
    - utter_vergonhaMedo
## Story esperanca
>check_relacaoViolenta
* esperanca
    - utter_esperanca
## Story isolamento
>check_relacaoViolenta
* isolamento
    - utter_isolamento
## Story negacao
>check_relacaoViolenta
* negacao
    - utter_negacao
## Story barreiras
>check_relacaoViolenta
* barreiras
    - utter_barreiras
## Story dependencia
>check_relacaoViolenta
* dependencia
    - utter_dependencia
## Story deixarAgressor
>check_relacaoViolenta
* deixarAgressor
    - utter_deixarAgressor


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

## Story mitosViolencia
>check_orientacao
* mitosViolencia
   - utter_mitosViolencia
>check_mitos
## Story mitoUm
>check_mitos
* affirm
   - utter_m1
   - utter_maisMitos
>check_mito1
## Story mitoDois
>check_mito1
* affirm
   - utter_m2
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito2
## Story mitoTres
>check_mito2
* affirm
   - utter_m3
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito3
## Story mitoQuatro
>check_mito3
* affirm
   - utter_m4
   - utter_maisSobre
* deny
   - utter_orientacao
>check_mito4
## Story mitoCinco
>check_mito7
* affirm
   - utter_m5
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito5
## Story mitoSeis
>check_mito9
* affirm
   - utter_m6
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito6
## Story mitoSete
>check_mito4
* affirm
   - utter_m4_7_Afirm
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito7
## Story mitoOito
>check_mito6
* affirm
   - utter_m8
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito8
## Story mitoNove
>check_mito5
* affirm
   - utter_m5_9_Afirm
   - utter_maisMitos
* deny
   - utter_orientacao
>check_mito9
## Story mitoDez
>check_mito8
* affirm
   - utter_m10
   - utter_orientacao

## Story_despedida
* goodbye
   - utter_goodbye
