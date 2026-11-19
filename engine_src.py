import json,os,sys,urllib.request
P,N,B,R,Q,K,OFF=1,2,3,4,5,6,7
VAL=(0,100,320,330,500,900,30000)
MATE,INF=30000,31000
KN=(-21,-19,-12,-8,8,12,19,21)
BI=(-11,-9,9,11)
RK=(-10,-1,1,10)
KQ=BI+RK
FILES="abcdefgh"
PROMCH="  nbrq"
SQ=tuple(21+10*r+c for r in range(8)for c in range(8))
MIR=[0]*120
for _s in SQ:
 MIR[_s]=21+10*(7-(_s-21)//10)+(_s-21)%10
def _X(*rows):
 return tuple(x for r in rows for x in(r+r[::-1]if len(r)==4 else r))
T_P=_X((0,0,0,0),(60,60,60,60),(12,14,24,32),(4,8,14,26),(0,2,8,20),(4,-4,-8,0),(4,8,8,-18,-18,10,10,4),(0,0,0,0))
T_N=_X((-48,-38,-28,-28),(-38,-18,0,0),(-28,0,12,16),(-28,4,16,22),(-28,0,16,22),(-28,4,10,16),(-38,-18,0,4),(-48,-38,-28,-28))
T_B=_X((-18,-8,-8,-8),(-8,0,0,0),(-8,0,6,10),(-8,6,6,10),(-8,0,12,10),(-8,10,10,10),(-8,6,0,0),(-18,-8,-8,-8))
T_R=_X((0,0,0,0),(8,12,12,12),(-4,0,0,0),(-4,0,0,0),(-4,0,0,0),(-4,0,0,0),(-4,0,0,0),(-2,0,2,6))
T_Q=_X((-16,-8,-8,-4),(-8,0,0,0),(-8,0,6,6),(-4,0,6,8),(0,0,6,8,8,6,0,-4),(-8,4,6,6,6,6,0,-8),(-8,0,4,0,0,0,0,-8),(-16,-8,-8,-4))
T_KM=_X((-30,-40,-40,-50),(-30,-40,-40,-50),(-30,-40,-40,-50),(-30,-40,-40,-50),(-20,-30,-30,-40),(-10,-20,-20,-20),(22,22,4,0),(24,34,12,0))
T_KE=_X((-50,-40,-30,-20),(-30,-20,-10,0),(-30,-10,20,30),(-30,-10,30,40),(-30,-10,30,40),(-30,-10,20,30),(-30,-30,0,0),(-50,-30,-30,-30))
PST=[None]*8
for _p,_t in((P,T_P),(N,T_N),(B,T_B),(R,T_R),(Q,T_Q),(6,T_KM),(7,T_KE)):
 _tab=[0]*120
 for _i,_v in enumerate(_t):
  _tab[21+10*(_i//8)+_i%8]=_v+(VAL[_p]if _p<6 else 0)
 PST[_p]=tuple(_tab)
KMG,KEG=PST[6],PST[7]
_x=0x9E3779B97F4A7C15
_z=[]
for _i in range(13*120+1):
 _x=(_x*6364136223846793005+1442695040888963407)&0xFFFFFFFFFFFFFFFF
 _z.append(_x)
ZP=tuple(_z)
ZSTM=_z[13*120]
def zk(p,s):
 return ZP[(p+6)*120+s]
BD=[OFF]*120
CAST=[0]
EP=[0]
KEY=[0]
SC=[0]
NPW=[0]
NPB=[0]
BIW=[0]
BIB=[0]
KW=[0]
KB=[0]
STM=[1]
CMASK=[15]*120
for _s,_v in((95,12),(98,14),(91,13),(25,3),(28,11),(21,7)):
 CMASK[_s]=_v
def load(fen):
 bd=[OFF]*20+sum(([OFF]+[0]*8+[OFF]for _ in range(8)),[])+[OFF]*20
 parts=fen.split()
 for r,row in enumerate(parts[0].split("/")):
  c=0
  for ch in row:
   if ch.isdigit():
    c+=int(ch)
   else:
    p="PNBRQK".find(ch.upper())+1
    bd[21+10*r+c]=p if ch.isupper()else-p
    c+=1
 BD[:]=bd
 STM[0]=1 if parts[1]=="w"else-1
 CAST[0]=0
 if len(parts)>2 and parts[2]!="-":
  for ch,bit in(("K",1),("Q",2),("k",4),("q",8)):
   if ch in parts[2]:
    CAST[0]|=bit
 EP[0]=0
 if len(parts)>3 and parts[3]!="-":
  EP[0]=21+10*(8-int(parts[3][1]))+FILES.find(parts[3][0])
 key=sc=npw=npb=biw=bib=0
 for s in SQ:
  p=bd[s]
  if not p:
   continue
  key^=zk(p,s)
  if p>0 :
   sc+=PST[p][s]
   if p not in(K,P):
    npw+=VAL[p]
  else:
   sc-=PST[-p][MIR[s]]
   if p not in(-K,-P):
    npb+=VAL[-p]
  if p==K:
   KW[0]=s
  elif p==-K:
   KB[0]=s
  elif p==B:
   biw+=1
  elif p==-B:
   bib+=1
 if STM[0]<0 :
  key^=ZSTM
 KEY[0]=key;SC[0]=sc
 NPW[0]=npw;NPB[0]=npb
 BIW[0]=biw;BIB[0]=bib
def atk(s,by):
 bd=BD
 for o in KN:
  if bd[s+o]==N*by:
   return True
 if bd[s+9*by]==P*by or bd[s+11*by]==P*by:
  return True
 for o in KQ:
  if bd[s+o]==K*by:
   return True
 for o in BI+RK:
  t=s+o
  q=bd[t]
  while q!=OFF:
   if q:
    a=q*by
    if a==Q or(a==B if o in BI else a==R):
     return True
    break
   t+=o
   q=bd[t]
 return False
def gen(caps):
 bd=BD
 stm=STM[0]
 cast=CAST[0]
 ep=EP[0]
 ms=[]
 ap=ms.append
 for f in SQ:
  p=bd[f]
  if p==0 or(p>0)!=(stm>0):
   continue
  a=p*stm
  if a==P:
   t=f-10*stm
   promo=t<30 or t>89
   if bd[t]==0 :
    if promo:
     for pr in(Q,R,B,N):
      ap(f|t<<7|pr<<14)
    elif not caps:
     ap(f|t<<7)
     if(stm>0 and 80<f<89)or(stm<0 and 30<f<39):
      if bd[f-20*stm]==0 :
       ap(f|(f-20*stm)<<7|1<<17)
   for o in(-9*stm,-11*stm):
    t=f+o
    q=bd[t]
    if q!=OFF and q*stm<0 :
     if promo:
      for pr in(Q,R,B,N):
       ap(f|t<<7|pr<<14)
     else:
      ap(f|t<<7)
    elif ep and t==ep:
     ap(f|t<<7|2<<17)
  elif a==N or a==K:
   for o in KN if a==N else KQ:
    q=bd[f+o]
    if q!=OFF and q*stm<=0 and(q or not caps):
     ap(f|(f+o)<<7)
  else:
   rays=BI if a==B else RK if a==R else KQ
   for o in rays:
    t=f+o
    q=bd[t]
    while q!=OFF:
     if q==0 :
      if not caps:
       ap(f|t<<7)
      t+=o
      q=bd[t]
      continue
     if q*stm<0 :
      ap(f|t<<7)
     break
 if not caps:
  if stm>0 and cast&3 and bd[95]==K:
   if cast&1 and bd[96]==0 and bd[97]==0 and bd[98]==R and not atk(95,-1)and not atk(96,-1):
    ap(95|97<<7|3<<17)
   if cast&2 and bd[94]==0 and bd[93]==0 and bd[92]==0 and bd[91]==R and not atk(95,-1)and not atk(94,-1):
    ap(95|93<<7|3<<17)
  elif stm<0 and cast&12 and bd[25]==-K:
   if cast&4 and bd[26]==0 and bd[27]==0 and bd[28]==-R and not atk(25,1)and not atk(26,1):
    ap(25|27<<7|3<<17)
   if cast&8 and bd[24]==0 and bd[23]==0 and bd[22]==0 and bd[21]==-R and not atk(25,1)and not atk(24,1):
    ap(25|23<<7|3<<17)
 return ms
def mk(m):
 bd=BD
 f=m&127
 t=(m>>7)&127
 pr=(m>>14)&7
 fl=m>>17
 p=bd[f]
 if fl==2 :
  cs=t+(10 if p>0 else-10)
  cap=bd[cs]
  bd[cs]=0
 else:
  cs=t
  cap=bd[t]
 bd[f]=0
 np_=pr*(1 if p>0 else-1)if pr else p
 bd[t]=np_
 if fl==3 :
  if t>f:
   bd[t-1],bd[t+1]=bd[t+1],0
   rf,rt=(98,96)if p>0 else(28,26)
  else:
   bd[t+1],bd[t-2]=bd[t-2],0
   rf,rt=(91,94)if p>0 else(21,24)
  rk_=bd[rt]
  if p>0 :
   SC[0]+=PST[R][rt]-PST[R][rf]
  else:
   SC[0]-=PST[R][MIR[rt]]-PST[R][MIR[rf]]
  KEY[0]^=zk(rk_,rf)^zk(rk_,rt)
 undo=(p,cap,CAST[0],EP[0],KEY[0],SC[0],NPW[0],NPB[0],
  BIW[0],BIB[0])
 CAST[0]&=CMASK[f]&CMASK[t]
 EP[0]=f-10 if fl==1 and p>0 else(f+10 if fl==1 else 0)
 if p>0 :
  SC[0]+=PST[p][t]-PST[p][f]
 else:
  SC[0]-=PST[-p][MIR[t]]-PST[-p][MIR[f]]
 if pr:
  if p>0 :
   SC[0]+=PST[np_][t]-PST[P][t]
   NPW[0]+=VAL[pr]
   if pr==B:
    BIW[0]+=1
  else:
   SC[0]-=PST[pr][MIR[t]]-PST[P][MIR[t]]
   NPB[0]+=VAL[pr]
   if pr==B:
    BIB[0]+=1
 if cap:
  a=cap if cap>0 else-cap
  if cap>0 :
   SC[0]-=PST[cap][cs]
   if a not in(K,P):
    NPW[0]-=VAL[a]
   if a==B:
    BIW[0]-=1
  else:
   SC[0]+=PST[a][MIR[cs]]
   if a not in(K,P):
    NPB[0]-=VAL[a]
   if a==B:
    BIB[0]-=1
  KEY[0]^=zk(cap,cs)
 if p==K:
  KW[0]=t
 elif p==-K:
  KB[0]=t
 KEY[0]^=zk(p,f)^zk(np_,t)^ZSTM
 STM[0]=-STM[0]
 return undo
def um(m,u):
 bd=BD
 f=m&127
 t=(m>>7)&127
 fl=m>>17
 p=u[0]
 bd[f]=p
 bd[t]=0 if fl==2 else u[1]
 if fl==2 :
  bd[t+(10 if p>0 else-10)]=-p
 elif fl==3 :
  if t>f:
   bd[t+1],bd[t-1]=bd[t-1],0
  else:
   bd[t-2],bd[t+1]=bd[t+1],0
 (CAST[0],EP[0],KEY[0],SC[0],NPW[0],NPB[0],
  BIW[0],BIB[0])=u[2 :]
 if p==K:
  KW[0]=f
 elif p==-K:
  KB[0]=f
 STM[0]=1 if p>0 else-1
ND=[0]
BG=[0]
TT={}
HC={}
KL=[[0,0]for _ in range(128)]
HS=[0]*16384
class Abort(Exception):
 pass
def qs(alpha,beta,ply):
 ND[0]+=1
 if ND[0]>=BG[0]:
  raise Abort
 if NPW[0]+NPB[0]<2600 :
  v=SC[0]+KEG[KW[0]]-KEG[MIR[KB[0]]]
 else:
  v=SC[0]+KMG[KW[0]]-KMG[MIR[KB[0]]]
 if BIW[0]>1 :
  v+=30
 if BIB[0]>1 :
  v-=30
 v=v*STM[0]+8
 if v>=beta:
  return v
 if v>alpha:
  alpha=v
 bd=BD
 ms=gen(True)
 scored=[]
 for m in ms:
  vic=bd[(m>>7)&127]
  s_=VAL[abs(vic)]*16 if vic else 0
  if m>>14 :
   s_+=VAL[m>>14&7]*4
  scored.append((-s_,m))
 scored.sort()
 for _,m in scored:
  if bd[(m>>7)&127]in(K,-K):
   return MATE-ply
  u=mk(m)
  v=-qs(-beta,-alpha,ply+1)
  um(m,u)
  if v>alpha:
   alpha=v
   if v>=beta:
    return v
 return alpha
def ab(depth,alpha,beta,ply):
 ND[0]+=1
 if ND[0]>=BG[0]:
  raise Abort
 if HC.get(KEY[0],0)>1 :
  return 0
 stm=STM[0]
 chk=atk(KW[0]if stm>0 else KB[0],-stm)
 if depth<=0 :
  if not chk:
   return qs(alpha,beta,ply)
  depth=1
 key=KEY[0]
 e=TT.get(key)
 ttm=0
 if e is not None:
  if e[0]>=depth:
   v=e[1]
   if v>=beta:
    return v
   if v>alpha:
    alpha=v
  ttm=e[2]
 if depth>=3 and not chk and ply and beta<MATE-500 and(NPW[0]if stm>0 else NPB[0]):
  ep0=EP[0]
  EP[0]=0
  KEY[0]^=ZSTM
  STM[0]=-stm
  v=-ab(depth-3,-beta,-beta+1,ply+1)
  STM[0]=stm
  KEY[0]^=ZSTM
  EP[0]=ep0
  if v>=beta:
   return beta
 ms=gen(False)
 if not ms:
  return-MATE+ply if chk else 0
 bd=BD
 k1,k2=KL[ply]if ply<128 else(0,0)
 scored=[]
 for m in ms:
  vic=bd[(m>>7)&127]
  if vic:
   s_=100000+VAL[abs(vic)]*16-VAL[abs(bd[m&127])]
  elif m>>14 :
   s_=100000
  elif m==ttm:
   s_=200000
  elif m==k1:
   s_=90000
  elif m==k2:
   s_=89000
  else:
   s_=HS[(m&127)*128+(m>>7)&127]
  scored.append((-s_,m))
 scored.sort()
 best=-INF
 bm=0
 for _,m in scored:
  if bd[(m>>7)&127]in(K,-K):
   return MATE-ply
  u=mk(m)
  v=-ab(depth-1,-beta,-alpha,ply+1)
  um(m,u)
  if v>best:
   best=v
   bm=m
   if v>alpha:
    alpha=v
    if v>=beta:
     HS[(m&127)*128+(m>>7)&127]+=depth*depth
     if ply<128 and k1!=m:
      KL[ply]=[m,k1]
     break
 if best<=-MATE+200 :
  return 0 if not chk else best
 if abs(best)<MATE-500 :
  TT[key]=(depth,best,bm)
 return best
def us(s):
 return FILES[(s-21)%10]+str(8-(s-21)//10)
def umv(u):
 f=21+10*(8-int(u[1]))+FILES.find(u[0])
 t=21+10*(8-int(u[3]))+FILES.find(u[2])
 pr=PROMCH.find(u[4])if len(u)>4 else 0
 p=BD[f]
 fl=0
 if p in(P,-P)and abs(t-f)==20 :
  fl=1
 elif p in(P,-P)and t==EP[0]and(t-f)%10 :
  fl=2
 elif p in(K,-K)and abs(t%10-f%10)==2 :
  fl=3
 return f|t<<7|pr<<14|fl<<17
def think(fen,legal,budget,moves=(),start=None):
 if start:
  load(start)
  HC.clear()
  HC[KEY[0]]=1
  for u in moves:
   mk(umv(u))
   HC[KEY[0]]=HC.get(KEY[0],0)+1
 else:
  HC.clear()
 load(fen)
 TT.clear()
 KL[:]=[[0,0]for _ in range(128)]
 HS[:]=[0]*16384
 legalset=set(legal)
 ND[0]=0
 BG[0]=budget
 stm=STM[0]
 root=[]
 rootu={}
 for m in gen(False):
  if BD[(m>>7)&127]in(K,-K):
   continue
  u=mk(m)
  ok=not atk(KW[0]if stm>0 else KB[0],-stm)
  um(m,u)
  if ok:
   s_=us(m&127)+us(m>>7&127)
   pr=m>>14&7
   if pr:
    s_+=PROMCH[pr]
   if s_ in legalset:
    root.append(m)
    rootu[m]=s_
 if not root:
  return legal[0]
 bestm=root[0]
 for d in range(1,64):
  cur=bestm
  root.sort(key=lambda m:m!=cur)
  a=-INF
  it_best=bestm
  try:
   for m in root:
    u=mk(m)
    v=-ab(d-1,-INF,-a,1)
    um(m,u)
    if v>a:
     a=v
     it_best=m
  except Abort:
   break
  bestm=it_best
  if a>MATE-500 :
   break
 return rootu[bestm]
def main():
 env=os.environ["MAKEFUN_ENV_URL"]
 def post(path,body):
  req=urllib.request.Request(
   env+path,data=json.dumps(body).encode(),
   headers={"content-type":"application/json"})
  with urllib.request.urlopen(req)as r:
   return json.load(r)
 while True:
  g=post("/game",{})
  if g["status"]=="done":
   break
  while g["status"]=="your_move":
   mv=think(g["fen"],g["legal_moves"],
    140000 if g["plies"]<60 else 90000
    if g["plies"]<120 else 50000,
    g.get("moves")or(),g.get("start_fen"))
   g=post("/move",{"game":g["game"],"move":mv})
main()
