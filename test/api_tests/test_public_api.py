import requests
import allure
import pytest

@allure.step('Call public API and check response')
def test_public_api():
    with allure.step('Send GET request to public API'):
        response = requests.get('https://api.github.com')
        assert response.status_code == 200
    with allure.step('Check response contains expected keys'):
        data = response.json()
        assert 'current_user_url' in data 

# --- Long stack trace failure example ---
def level_one():
    with allure.step('Level 1'):
        level_two();
        level_five()

def level_two():
    with allure.step('Level 2'):
        level_three()

def level_three():
    with allure.step('Level 3'):
        level_four()

def level_four():
    with allure.step('Level 4'):
        level_five()

def level_five():
    with allure.step('Level 5 - fail here'):
        assert False, 'This is a forced failure for stack trace demonstration.'

@allure.step('Test with nested steps')
def test_api_nested_steps():
    level_one() 

@allure.step('Test with ascii art')
def test_stacktrace_ascii_art():
    assert False, r"""
 ________________________________________
/ You have Egyptian flu: you're going to \
\ be a mummy.                            /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

@allure.step('Test with enourmous stack trace')
def test_stacktrace_enourmous():
    assert False, r"""
    M.                                          .:M
    MMMM:.                                   .:MMMM
    MMMMMMMM:..                           .:MMMMMMM
    :MMHHHMMMMHMM.   .:MMMMMMMMM:.      .:MMHHMHMM:
     :MMHHIIIHMMMM.:MMHHHHIIIHHM MMM. .::MMHIHIIHHM:
      MMMHIIIIHHMMMIIHHMHHIIIIIHHMMMMMMMHHHIIIIHHM:
      :MMHIIIIIHMMMMMMMHHIIIIIIHHHMMMMMMHHII:::IHM.
       MH:I:::IHHMMMMMHHII:::IIHHMMMHHHMMM::I:IHMM
       :MHI:HHIHMMHHIIHII::.::IIHMMHHIHHMMM::HMMM:
        MI::HHMMIIM:IIHII::..::HM:MHHII:::IHHMMM:
        MMMHII::..:::IHMMHHHHMHHMMI:::...::IHM:
        :MHHI::....::::HMMMMMMHHII::.. ..::::M:
         :MI:.:MH:.....:HMMMMHHMIHMMHHI:HH.:MM
         M:.I..MHHHHHMMMIHMMMHMMHHHHHMMHHH.:MM.
         :M:HM:.M I:MHIIMMIIHM I:MM::.:MMI:M..
         'M::MM:IMH:MMII MMHIMHI :M::IIHMM:MM
          MH:HMMHIHMMMMMMHMMIMHIIHHHHIMMHHMM
           MI:MMMMHI:::::IMM:MHI:::IMMMMHIM
            MH:MMMHHHHHI:HMMHMMIHHMMMMMHIM
            :IMHIHMMMMMM:MMMMMHHHHMMMHI:M
             HI:IMIHMMMM:MMMMMMHHHMI:.:M
.............M::..:HMMMMIMHIIHMMMMHII:M:::'''''''''''
      ....:::MHI:.:HMMMMMMMMHHHMHHI::M:::::::'''''''
   '''   ...:MHI:.::MMHHHMHMIHMMMMHH.MI..........
     '''  ....MHI::..:MHHHHIHHMM:::IHM          ''''
             IMH.::..::HMMHMMMH::..:HM:
            :M:.H.IHMIIII::IIMHMMM:H.MH
             IMMMH:HI:MMIM:IHI:HIMIHM::
           .MMI:.HIHMIMI:IHIHMMHIHI:MIM.
          .MMHII:::IHIII::::::IIIIIIHMHII
          MHHHI::.:IHHII:::.:::IIIIHMIIHM:
         MHHHII::..::MII::.. ..:IIIHHHII:IM.
        .MHHII::....:MHII::.  .:IHHHI::IIHMM.
        MMHHII::.....:IHM:. ..:IIHII::..:HHMM
        MHHII:::......:IIHI...:IHI::.....::HM:
       .MHHI:::.........:III..II::... ...:IHMI
       :MMH:::........ ...::..::....  ...:IHMM
       IMHIII:::..........      .........::IHM.
       :MHIII::::......           .......::IHMM
        MHHIII::::..               ......::IHM:
        IMHHIII:::...              .....::IIHMM
        :MHHIII:::I:::...      ....::::I::IIHMM
         MMHHIII::IHI:::............:::IIH:IHMM
         :MMHHII:IIHHI::::::.....::::::IH:IIHM:.
          MMMHHII:IIHHI:::::::::::::IHI:IIM:MM::
          MMMHHIII::IHHII:::::::::IHI:IIIHMM:MM:
          :MMHHHIII::IIIHHII::::IHI..IIIHHM:MHMM
          :MMMHHII:..:::IHHMMHHHHI:IIIIHHMM:MIM.
          .MMMMHHII::.:IHHMM:::IIIIIIHHHMM:MI.M
        .MMMMHHMHHII:::IHHMM:::IIIIIHHHHMM:MI.IM.
      .MMMHMMMHHHII::::IHMM::IIIHHMMMMM::MMMMHHHMM.
    .MMMHHMHMHHII:::.::IHMM::IIIIHHHMMMM:MMH::IHMMM
    :MHIIIHMMHHHII:::IIHMM::IIIHHMMMMM:::MMMMHHHHMM.
    MMHI:IIHMMHHHI::::IHMM:IIIIHHHMMMM:MMMHI::IMMMM.
    MMH:::IHMMHHHHI:::IHMM:IIIHHHHMMMM:MMHI:.:IHHMM.
    :MHI:::IHMHMHHII::IHMM:IIIHHHMMMMM:MHH::.::IHHM::
    'MHHI::IHMMHMHHII:IHMM:IHMMHHHMMMM:MMHI::.::IHHMM:
     :MHII:IIHMHIHHIIIIHMM:IIHHHHMMMM:MHHI:...:IIHMMM:
     'MHIII:IHHMIHHHIIHHHMM:IHHHMMMMM:MHHI:..::IIHHMM
      :MHHIIIHHMIIHHHIHHHMM:HHHHMMMMM:MHII::::IIIHHMM
       MHHIIIIHMMIHHHIIHHMM:HHHHMMMM:MMHHIIHIIIIIHHMM.
       'MHHIIIHHMIIHHIIIHMM:HHHMMMMH:MHHMHII:IIIHHHMM:
        'MHHIIIHMMIHHHIHHMM:HHHMMMHH:MMIMMMHIIIHHMMMM:
         'MHHIIHHMIHHHHHMMM:HHHMMMH:MIMMMMMMMMMMHIHHM:
          :MHHIIHMIHHHHHMMM:HHHMMMM:MMHMMHIHMHI:IHHHM
           MHHIIHM:HHHHHMMM:HHHMMMM:MMMHIHHIHMM:HHIHM
            MHHIHM:IHHHHHMM:HHHHHMM:MMHMIIHMIMMMIHIM:
            :MHIHMH:HHHHMMM:HHHHMM:MMHIIHMIIHHIMMHIM'
             MMHHMH:HHHHHMM:HHHHMM:MHHHHIMMHII::IHMH:
             'MMMMH:HHHHHMM:HHHHMM:MHHIHMMIIIHMHIMM:
              :MMHM:HHHHHMM:HHHHMM:MHIHIMMMHIHHIMIH:
               MMMM:HHHHHMM:HHHHHM:MHHMIMMMHHHHHIM:MMMMM.
               :MMM:IHHHMMM:HHHHMM:MHHHIIMMMIIMIM:MMMMMMM:
               :MMM:IHHHHM:HHHHMMM:MMHHHIHHMMMMM:MMMMMMMMM
                MHM:IHHHMM:HHHMMMM:MMHHHHIIIHHHIIIMMMMMMMM
                MHM:IHHHMM:HHHMMMM:HMMMHHHHHHHMMMMMMMMMMM:
                MHM:IHHHHM:HHHHHMM:HHHMMMMMHHHHMMMMMMMMM'
           .MI:.MMM:IMHHIM:MMHMMMMMMHHHHIMHIMMHHHHHMMMM'
          :IM:MMMMIM:M:MMM:MMHHHHHIHIHMMHIHMMHHHHHHMMM'
          :IM:M:MIM::M:HM:IMHIM:IM:M:MIHHHIMMMMMMMMMM'
           'M:MHM:M:MM:MMHIMHHIHMI      '::MMMMMMM:'
              'M'MHMM'M''MMHI'MMH'
"""