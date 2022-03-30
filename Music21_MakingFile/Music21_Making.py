from music21 import *

#기본지식 레퍼런스 : https://web.mit.edu/music21/doc/moduleReference/moduleBase.html

# --- musescore 3을 이용하기 위한 path 설정
us = environment.UserSettings()
us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'
us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'

# --- 사용할 MIDI data의 path 설정
datapath = "C:/Users/car99/PycharmProjects/pythonProject1/캡스톤디자인/MIDI/Canon_in_D.mid"
datapath2 = "C:/Users/car99/PycharmProjects/pythonProject1/캡스톤디자인/MIDI/Gossec_Gavotte_in_D_major.mid"
midi = converter.parse(datapath)
midi2 = converter.parse(datapath2)

#midi 안에 2개의 파트 , 파트 안에 수백개의 마디

make = stream.Stream()
str1 = midi.parts.stream()
str2 = midi2.parts.stream()

hi = stream.Part()
lw = stream.Part()
h = stream.Measure([clef.TrebleClef()])
l = stream.Measure([clef.BassClef()])
h.timeSignature = meter.TimeSignature('4/4')
l.timeSignature = meter.TimeSignature('4/4')

hi.append(h)
lw.append(l)

rand1 = [3,5,2,4,9,6,8,7,10,13,12,16,11,15,14]
rand2 = [7,8,9,4,6,5,2,3,13,12,10,16,15,11,14]

ch1 = str1[1].chordify()
ch2 = str2[0].chordify()

for i in ch1:
    print(i)


for i in range(len(rand1)):
    p = rand1[i]
    hi.append(ch2[p])

for i in range(len(rand2)):
    p = rand2[i]
    lw.append(ch1[p])


make.append(hi)
make.append(lw)
make.show()


#정리하면 악보 > Part > 마디 > 마디안의 음표 , 셈여림표 , 높은 낮은 음자리표 등등이다.
#즉 악보를 하나 만드려면 뒤쪽부터 구성해서 하나로 합쳐야 한다는 것이다.

#make = stream.Stream() > hi = stream.Part(),lw = stream.Part() >
#h = stream.Measure([clef.TrebleClef()]) , l = stream.Measure([clef.BassClef()])
#clef는 음자리표로 미리 처음에 넣어준 것이다.

#요소들도 걷어낼 건 걷어내고 해야할 듯
#보니까 셈여림표 부터 순수한 음표를 제외하고 다른 부분이 많이 개입하고 있음


#-------

#어울리는 코드끼리 결합해보기?

#곡을 4부분 8부분 이런식으로 토막냄 -> 그 토막의 특징을 모델이 학습함 ->
#마디간의 특징을 뽑아낼 수 있다면? => ex) 마디의 ( 높은 , 낮은 ) 주 코드 , ( 높은 , 낮은 ) 서브 코드 , 박자 나열 등등
#대부분 곡들이 파트 ABCD...로 구분할 수 있다. 그렇다면 마디별로 파트 라벨링을 하고 해당되는 파트에 나올 가능성이 높은 방식으로
#구성?

#예를 들어 마디 10개가 있으면 3개는 A , 3개는 B , 2개는 C , 2개는 D 라고 하자.
#그렇다면 , A안에 3개의 마디별로 특징을 뽑고 그 특징들을 모아 A의 특징을 뽑아낼 수 있을 것이다.

#이를 시계엘 데이터와 연결해서 A 파트 안에서 마디의 나열이 전 마디에 영향을 받아서 나올 수 있도록 구성
#파트 A에서는 이러한 특징의 마디 뒤에 이러한 특징의 마디가 어떤 확률로 나왔고 , 이런식으로?

#현재 기술도 ai에게 인간이 다시 피드백을 주고 그로써 학습하는데 , 이 부분을 떨칠 수 있나?

#시계열 데이터 : Autoencoder는 모델의 input과 output이 같은 모델
#이러한 배경으로 딥러닝(특히 RNN 계열)은 시계열 데이터에서 가지고 있는 특유의 긴 sequence에 걸쳐있는 패턴을 추출하는데 잘 작동합니다.
