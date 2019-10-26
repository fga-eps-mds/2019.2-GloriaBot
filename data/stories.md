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