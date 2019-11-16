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
* facaExt
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
* ameacarFilhos
    - utter_agressorFilhosAlto
## Story AgressorFilhosExtremo
>check_AgressorFilhosAffirm
* baterFilhos
    - utter_agressorFilhosExtremo
    - utter_delegacia

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