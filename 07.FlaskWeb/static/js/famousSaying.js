window.onload = function () {


    let says = [

'성공으로 가는 엘리베이터는 고장입니다. 당신은 계단을 이용해야만 합니다. 한계단 한계단씩.',
'유머를 정의하고 분석하는 것은 유머 없는 사람들의 취미다.',
'인생은 자전거를 타는 것과 같다. 균형을 잡으려면 움직여야 한다. 인생은 본래 녹록지 않다. 하지만 멍청한 사람에게는 더욱 녹록지 않다.',
'나는 행동이 사람의 생각을 가장 훌륭하게 해석해 준다고 늘 생각해왔다. 나는 법을 가르칠 수 없는 자에게는 더 빨리 추락하는 법을 가르쳐라!',
'문제는 어떻게 새롭고 혁신적인 생각을 하느냐가 아니라 어떻게 오래된 생각을 비워내느냐 하는 것이다. 모든 사람의 머릿속은 케케묵은 가구로 가득찬 건물과 같다. 한쪽 구석을 비워낸다면 창의성이 즉시 그 자리를 메울 것이다.',
'친구의 충고는 신중하게 곱씹어 받아들여야 한다. 옳건 그르건, 자신의 생각을 포기하고 친구의 충고를 무조건 따라서는 안된다.',
'당신을 만나는 모든 사람이 당신과 헤어질 때는 더 나아지고 더 행복해질 수 있도록 하라.',
'매일 아침 하루 일과를 계획하고 그 계획을 실행하는 사람은, 극도로 바쁜 미로 같은 삶 속에서 그를 안내할 한 올의 실을 지니고 있는 것이다. 그러나 계획이 서있지 않고 단순히 우발적으로 시간을 사용하게 된다면, 곧 무질서가 삶을 지배할 것이다.',
'잘못된 열정을 통제하는 것보다는 배제하는 것이, 잘못된 열정에 휩싸인 후에 마음을 다잡는 것보다는 휩싸이지 않도록 하는 것이 더 쉽다.',
'가장 용감한 행동은 자신만을 생각하는 것이다. 큰 소리로.',
'가지고 있는 어떤 재주든 사용하라. 노래를 가장 잘하는 새들만 지저귀면 숲은 너무도 적막할 것이다.',
'사실, 인생의 어느 같은 시점에서 돈을 벌기 위한 회의에 참석하는 동시에 그 돈을 기부하기 위해 다른 회의에 가는 것은 다소 혼란스러우리라 생각했다.',
'제대로 배우기 위해서는 거창하고 교양 있는 전통이나 돈이 필요하지 않다. 스스로를 개선하고자 하는 열망이 있는 사람들이 필요할 뿐이다.',
'중요한 것은 학습을 중단하지 않고, 도전을 즐기고, 애매모호함을 받아들이는 것이다. 종국에는 확실한 해답은 없기 마련이다.',
'개인은 천재다. 그러나 군중은 머리없는 괴수, 거대하고 야수같은 바보가 되어 시키는 대로 행동한다.',
'최선을 다하고 있다라고 말해봤자 소용없다. 필요한 일을 함에 있어서는 반드시 성공해야 한다.',
'성공에는 비밀이 없다. 성공한 사람 치고 성공에 대해 말하지 않는 사람을 본적 있는가?',
'창의성이란… 아직 존재하지 않는 것을 보는 것이다. 그것을 존재하도록 하는 방법을 찾아내고 그렇게 신의 친구가 되는 것이다.',
'만약 사람이 살면서 새 친구를 사귀지 않는다면, 곧 홀로 남게 될 것이다. 사람은 우정을 계속 보수해야 한다.',
'산, 강, 그리고 도시만을 생각한다면 세상은 공허한 곳이지만, 비록 멀리 떨어져 있더라도 우리와 같이 생각하고 느끼는 그 누군가가 있다는 사실을 알면 지구는 사람이 사는 정원이 될 것이다.',
'인생에서 인간이 가질 수 있는 모든 것은 가족과 친구라는 것을 알게 되었다. 이들을 잃게 되면 당신에겐 아무것도 남지 않는다. 따라서 친구를 세상 그 어떤 것 보다 더 소중하게 여겨야 한다.',
'가장 발전한 문명사회에서도 책은 최고의 기쁨을 준다. 독서의 기쁨을 아는 자는 재난에 맞설 방편을 얻은 것이다.',
'독서가 정신에 미치는 효과는 운동이 신체에 미치는 효과와 같다.',
'한 권의 책을 읽음으로써 자신의 삶에서 새 시대를 본 사람이 너무나 많다.',
'작별 인사에 낙담하지 말라. 재회에 앞서 작별은 필요하다. 그리고 친구라면 잠시 혹은 오랜 뒤라도 꼭 재회하게 될 터이니.',
'내일은 인생에서 가장 중요한 것이다. 자정이 되면 내일은 매우 깨끗한 상태로 우리에게 다가온다. 매우 완벽한 모습으로 우리 곁으로 와 우리 손으로 들어온다. 내일은 우리가 어제에서 뭔가를 배웠기를 희망한다.',
'냄새는 수천 마일 밖과 그동안 살아온 모든 세월을 가로질러 당신을 실어 나르는 강력한 마법사다.',
'현재뿐 아니라 미래까지 걱정한다면 인생은 살 가치가 없을 것이다.',
'최고가 되기 위해 가진 모든 것을 활용하세요. 이것이 바로 현재 제가 사는 방식이랍니다.',
'우리가 계획한 삶을 기꺼이 버릴 수 있을 때만, 우리를 기다리고 있는 삶을 맞이할 수 있다.',
'가장 위대한 영광은 한 번도 실패하지 않음이 아니라 실패할 때마다 다시 일어서는 데에 있다.',
'절대 허송세월 하지마라. 책을 읽든지, 쓰든지, 기도를 하든지, 명상을 하든지, 또는 공익을 위해 노력하든지, 항상 뭔가를 해라.',
'도전은 우리로 하여금 새로운 무게중심을 찾게 하는 선물입니다. 맞서 싸우지 마세요. 그저 중심을 잡을 수 있는 다른 방법을 찾아보세요.',
'할 수 없을 것 같은 일을 하라. 실패하라. 그리고 다시 도전하라. 이번에는 더 잘 해보라. 넘어져 본 적이 없는 사람은 단지 위험을 감수해 본 적이 없는 사람일 뿐이다. 이제 여러분 차례이다. 이 순간을 자신의 것으로 만들라.',
'도전은 인생을 흥미롭게 만들며, 도전의 극복이 인생을 의미있게 한다.',
'인생을 돈벌이에만 집중하는 것은 야망의 빈곤을 보여주는 것이다. 네 스스로에게 너무 적은 것을 요구하는 것이다. 야망을 가지고 더 큰 뜻을 이루고자 할 때에야 비로소 진정한 자신의 잠재력을 실현할 수 있기 때문이다.',
'재능이 있거든 가능한 모든 방법으로 사용하라. 쌓아두지 마라. 구두쇠처럼 아껴 쓰지 마라. 파산하려는 백만장자처럼 아낌없이 써라.'
    ];
    
    
    document.getElementById('famoussaying').innerHTML = says[Math.floor(Math.random() * says.length)];
}