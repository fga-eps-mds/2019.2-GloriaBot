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
## Story mitosViolencia
>check_orientacao
* mitosViolencia
    - utter_mitosViolencia
## Story mitoUm
* m1
    - utter_m1
## Story mitoDois
* m2
    - utter_m2
## Story mitoTres
* m3
    - utter_m3
## Story mitoQuatro
* m4
    - utter_m4
## Story mitoCinco
* m5
    - utter_m5
## Story mitoSeis
* m6
    - utter_m6
## Story mitoSete
* m4_7_Afirm
    - utter_m4_7_Afirm
## Story mitoOito
* m8
    - utter_m8
## Story mitoNove
* m5_9_Afirm
    - utter_m5_9_Afirm
## Story mitoDez
* m10
    - utter_m10