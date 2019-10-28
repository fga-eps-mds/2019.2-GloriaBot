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
>check_mitoQuatro
## Story mitoCinco
>check_mitos
* m5
    - utter_m5
>check_mitoCinco
## Story mitoSeis
>check_mitos
* m6
    - utter_m6
## Story mitoSete
>check_mitoQuatro
>check_mitos
* m4_7_Afirm
    - utter_m4_7_Afirm
## Story mitoOito
>check_mitos
* m8
    - utter_m8
## Story mitoNove
>check_mitos
>check_mitoCinco
* m5_9_Afirm
    - utter_m5_9_Afirm
## Story mitoDez
>check_mitos
* m10
    - utter_m10
## Story Aguentam_Relacao_Violenta
* AguentamRelacaoViolenta1
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