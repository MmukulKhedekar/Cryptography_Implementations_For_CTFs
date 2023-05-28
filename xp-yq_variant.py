from Cryptodome.Util.number import *

c = 8755361716037050593786802368740593505819541985087751465246316611208654712808851039985566950771569219005474679214890773248679686452291791926024778938667161954201119658253063645930886986362437085401598314742279109631478572452731396671691672092589080935682736804089015740009401298581639291193682963105747576715867254889247753788661315475189523656612126700002888122729034598825641796362628516626027115516263101484541445062801096777586863144812446160024700491104414848804200440962708078212109059521089126401730984744470907608297401873174614500873021527030728187991640911253978614160956515292658729861625177800745954684779
k = -34384571636542682732993801408238567193071079747335767504994340801608381182708103244757509021281874449800069281009810023907313154391464668542796187787092864913072601227852655851070468919417844230689008922504112542853587185699616544272977753830325804164014338601030700848859059311067280180340700746209053062443574270773642918163909645688335979566572624221870500744676835269869601108253139361167400301626751736498534338162228764111438600887057835670459016374249012923832476577336962810182684197767760519515721734005603313785840044947657687083840236225406435252382559823958066573244309719575485706011861244028446996920249519039258733914177844818916938491744948605478385399858626470926733928838196963004350577779862247581837961536832869640531493345914188439519605065799034864280428993112773164769200946009507688445375319097127445639570984261253620532620742924894113105707671949166533244311479026914960105181835442456417671355468402543233569770391833669600663695797387468169339523234585262610811933566181920470444240902853887724615316068488136323539979229581225786468457662315990029857258798124732280829662164932213109363870409335054243794586400741357324161913978437694775195815062757093213325952057171001722380372888748256174953952360070118846290246140793770694204401164960742113068366766928707670654861609748340943116513275092360152185494867472310293656556031756417497249251872489238008435654320326489069126549344443700948553988405022863350434081213995337512472150109078421242823877306926652997021828653860169896336216359386864067959578257760
r = 936281797755031261848169861788419286242500155122743234286943102853441400861252708389579924384747328538959760271792565686537791395731078897913727180911468908585976003090733895007958447959094383445975201070786043510921764921108055952715166472860417830673976831707347242236348495245218675030438657044803590841511241481934488468486944285639180440843969944429852785215880499136631346605823164121032336218990671202212953326203467124685189344280256775009299633701974115736573067349919745244858804283455071851912194286160784172943301316083821185405338610368688605358644365423958890024208974121167171384473118059281816494356755844809173265412809337423995268268663119244396063406978295035815869788202375167281450339517979957331467143500209528727150295191004885385839900735810500718557821053671052959432831767663810090095379231750412744076404163742435544440795801122979274805554706606583599755007872912935576369508808550677885164226933064726817359773399072956113665969905205606138989373281554161008535232454798115570092928010969726174633824544610380764744958638537085759378694993737437724201369828812993239842742165386297807164278219508640684529837977445571884153238673179892479261196341148157129952993380440229458239746064451443526116917519
s = 834939575457003657728171346390813480312906155291642219227936205156714217262322467739149680558607905413429343953514849176130680023475055635457415545359365246681638783469216604913252838569701559353464582588062109434066644004845623203772527840551656611501677400844706770270825409839625738792427657150026307314821780392251524458037197655903343177131336842583042394801173673131588262961636245185030505564613639234805815677902379543111678201103954034310087231196210755934978052370451876638256180762443170329319207101581789208664345386093469896758682416555125087939413443536267912794750486701814941395277218714280572422080584205069255289731982911845911942205319661268893590368592905932152208108183590473584581786595300724772852979382943318977777850080673301763071986653891789753006523321672813311922284194072995019342531330632536316816984745914614649167801364562670569095961614178729268507876040470655722687777049415470890053491272405716858536141212596151075134173517337948569646361076821140748265156759845142133374048339524320025708823936755215461004080494169096216330198356553864601197456450193436851885342802515269136267023694614035998000939158575602883575921465198767978819627846523739073812562683002815460930245515210169007766320597
# r*p - s*q = k
x = (k+s)%s
y = (r-k)%r
p = (pow(r,-1,s)*x)%s
q = (pow(s,-1,r)*y)%r
phi = (p-1)*(q-1)
e=0x10001
print(long_to_bytes(pow(c,pow(e,-1,phi),p*q)))

# b'grey{H3y_B@by_YouBetterBecomeDoktar!_7g9vpBA489mKYkg9}'