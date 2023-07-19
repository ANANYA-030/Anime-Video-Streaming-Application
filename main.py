from tkinter import *
from functools import partial
from tkVideoPlayer import TkinterVideo
import time
from ffpyplayer.player import MediaPlayer
 
window=Tk()
window.geometry("650x548")
window.title("Anime streaming application")
window.config(background="black")
canvas= Canvas(window,height=548,width=650)
background_photo=PhotoImage(file='photos\\bgimg.png')



 
def click():
  welcomeText.destroy()
  button.destroy()
  animePage()
 
def home():
  canvas.delete("all")
  #frame.destroy()
  NameLabel.destroy()
  animePage()

def Play(name,info,path):
  canvas.delete("all")
  topAiringLabel.destroy()
  popularLabel.destroy()
  animePlay(name,info,path)

def destroy():
  canvas.delete("all")
  topAiringLabel.destroy()
  popularLabel.destroy()
'''
def purtohome():
  canvas.delete("all")
  heading2.destroy()
  animePage()
'''
def rectohome():
  canvas.delete("all")
  heading1.destroy()
  animePage()
'''
def Purchase():
  destroy()
  canvas.create_image(0,0,image=background_photo,anchor='nw')
  home_btn=Button(canvas,text="HOME",bg="blue",borderwidth=3,command=purtohome)
  canvas.create_window(600,68,window=home_btn) 
  global heading2
  heading2=Label(canvas,text="Purchase History",fg="white",bg="blue",font=('Arial',25,'bold'),width=32,height=1)
  heading2.place(x=2,y=5)   
'''
def recprint():


  canvas.create_text(300,290,text="Recommending anime to watch based on choice:",font=("Helvetica",20),fill='Pink')
  if(var.get()==5):
    
    canvas.create_text(140,350,text="Demon Slayer\nNaruto Shippuden",font=("Helvetica",20),fill='white')
    radiobtn2[1].configure(state='disabled')
  elif var.get()==6:
    
    canvas.create_text(140,350,text="Blue lock",font=("Helvetica",20),fill='white')
    radiobtn2[0].configure(state='disabled')
  elif var.get()==3:
    
    canvas.create_text(140,350,text="Spy X Family Part-1\nSpy X Family Part-2",font=("Helvetica",20),fill='white')
    radiobtn2[1].configure(state='disabled')
  elif var.get()==4:
    
    canvas.create_text(140,350,text="One Piece",font=("Helvetica",20),fill='white')
    radiobtn2[0].configure(state='disabled')

def selection():
  global var,ques2,radiobtn2
  radiobtn2=[]
  var=IntVar()
  if(v.get()==1):
    radiobtn1[1].configure(state='disabled')
    ques2=Label(canvas,text="2.Do you prefer action or sports genere?",fg="white",bg="pink",font=('Arial',15,'bold'),width=53,height=1)
    canvas.create_window(325,200,window=ques2)
    values={"Action":5,
          "Sports":6}
    k=50
    count=0
    for text in values:
      radiobtn2.append(Radiobutton(canvas,text=text,variable=var,value=values[text],command=recprint))
      canvas.create_window(k,260,window=radiobtn2[count])
      k=k+100
      count=count+1

    '''
    qo1=Radiobutton(canvas,text="Action",variable=var,value=1,command=print)
    qo1.place(x=13,y=250)
    qo2=Radiobutton(canvas,text="Sports",variable=var,value=2,command=print)
    qo2.place(x=100,y=250)
    '''
  else:
    radiobtn1[0].configure(state='disabled')
    ques2=Label(canvas,text="2.Do you prefer anime with less episodes or more?",fg="white",bg="pink",font=('Arial',15,'bold'),width=53,height=1)
    canvas.create_window(325,200,window=ques2)
    values={"Less":3,
          "More":4}
    k=50
    count=0
    for text in values:
      radiobtn2.append(Radiobutton(canvas,text=text,variable=var,value=values[text],command=recprint))
      canvas.create_window(k,260,window=radiobtn2[count])
      k=k+100
      count=count+1

    '''
    qo3=Radiobutton(canvas,text="Less",variable=var,value=3,command=print)
    qo3.place(x=13,y=250)
    qo4=Radiobutton(canvas,text="More",variable=var,value=4,command=print)
    qo4.place(x=100,y=250)
    '''



def recPage():
  destroy()
  global v,o1,o2,ques1,radiobtn1
  v=IntVar()
  canvas.create_image(0,0,image=background_photo,anchor='nw')
  home_btn=Button(canvas,text="HOME",bg="blue",borderwidth=3,command=rectohome)
  canvas.create_window(600,68,window=home_btn) 
  global heading1
  heading1=Label(canvas,text="Anime Recommender",fg="white",bg="blue",font=('Arial',25,'bold'),width=32,height=1)
  heading1.place(x=2,y=5)   
  ques1=Label(canvas,text="1.How are you feeling now?",fg="white",bg="pink",font=('Arial',15,'bold'),width=54,height=1)
  canvas.create_window(328,100,window=ques1)
  values={"Happy":1,
          "Sad":2}
  radiobtn1=[]
  k=50
  count=0
  for text in values:
    radiobtn1.append(Radiobutton(canvas,text=text,variable=v,value=values[text],command=selection))
    canvas.create_window(k,150,window=radiobtn1[count])
    k=k+100
    count=count+1
  ''' 
  o1=Radiobutton(canvas,text="Happy",variable=v,value=1,command=selection)
  o1.place(x=13,y=140)
  o2=Radiobutton(canvas,text="Sad",variable=v,value=2,command=selection)
  o2.place(x=100,y=140)
  '''


def play_pause():
  if videoplayer.is_paused():
    videoplayer.play()
    player.set_pause(False)
    play_pause_btn["text"]="Pause"
  else:
    player.set_pause(True)
    videoplayer.pause()
    play_pause_btn["text"]="Play"

def back(name,info,pathlist):
  videoplayer.destroy()
  player.close_player()
  play_pause_btn.destroy()
  back_btn.destroy()
  animePlay(name,info,pathlist)

def video(name,info,path,pathlist):
  canvas.delete("all")
  NameLabel.destroy()
  global player,videoplayer,play_pause_btn,back_btn
  videoplayer=TkinterVideo(scaled=True,master=canvas)
  player=MediaPlayer(path)
  videoplayer.load(path)
  time.sleep(2) 
  videoplayer.pack(expand=True,fill="both")
  videoplayer.play()

  play_pause_btn=Button(canvas,text="PAUSE",bg="blue",command=play_pause)
  play_pause_btn.pack() 
  back_btn=Button(canvas,text="BACK",bg="blue",command=partial(back,name,info,pathlist))
  back_btn.pack()







def animePlay(name,info,path):
    pathlist=path
    canvas.create_image(0,0,image=background_photo,anchor='nw')

    home_btn=Button(canvas,text="HOME",bg="blue",borderwidth=3,command=home)
    canvas.create_window(600,70,window=home_btn)
    
    global NameLabel
    NameLabel=Label(canvas,text=name,fg="white",bg="blue",font=('Arial',25,'bold'),width=32,height=1)
    NameLabel.place(x=2,y=5)   
    #canvas.create_text(210,40,text=name,font=("Helvetica",35,'bold'),fill='red')
    canvas.create_text(140,120,text=info,font=("Helvetica",20),fill='Pink')
    canvas.create_text(70,220,text="EPISODES",font=("Helvetica",20,'bold'),fill='orange')
    '''
    ep_btn=Button(canvas,text="EPISODE 1",bg="green",borderwidth=3,command=count)
    ep_btn_window=canvas.create_window(100,250,window=ep_btn)
    '''
    #purchase_list=[]
    #if not purchase_list:
      #pur_btn=Button(canvas,text="PURCHASE",bg="green",borderwidth=3,command=purchase_list.append("hi"))
      #pur_btn_window=canvas.create_window(50,260,window=pur_btn)
    #else:
    epibtn=[]
    j=260
    k=0
    for i in range(1,4):
      epibtn.append(Button(canvas,text="EPISODE"+str(i),bg="blue",borderwidth=3,command=partial(video,name,info,path[i-1],pathlist)))
      canvas.create_window(50,j,window=epibtn[k])
      j=j+30
      k=k+1
   





    #global frame
    #frame = Frame(canvas)
    #frame.place(x=20,y=240)
    #for i in range(1,4):
     # Button(frame,text="EPISODE"+str(i),bg="green",borderwidth=3,command=count).pack()
      
    window.mainloop()
 
def animePage():
  global topAiringLabel,popularLabel
  topAiringLabel=Label(canvas,text="TOP AIRING",fg="white",bg="black",width=91,height=2)
  popularLabel=Label(canvas,text="POPULAR",fg="white",bg="black",width=91,height=2)

  recommend_btn=Button(canvas,text="Recommender",bg="blue",borderwidth=3,command=recPage)
  canvas.create_window(60,30,window=recommend_btn)
    
  #purchase_btn=Button(canvas,text="Purchase histroy",bg="blue",borderwidth=3,command=Purchase)
  #canvas.create_window(585,30,window=purchase_btn)
    

  global v1,v2
  v1=[["videos\\spy1_1.mkv","videos\\spy1_2.mkv","videos\\spy1_3.mp4"],
      ["videos\\demon_1.mp4 ","videos\\demon_2.mp4 ","videos\\demon_3.mp4 "],
      ["videos\\naruto_1.mkv","videos\\naruto_2.mkv","videos\\naruto_3.mkv"]]
  
  
  v2=[["videos\\naruto_1.mkv","videos\\naruto_2.mkv","videos\\naruto_3.mkv"],
      ["videos\\blue_1.mp4","videos\\blue_2.mkv","videos\\blue_3.mkv"],
      ["videos\\spy2_1.mp4","videos\\spy2_2.mkv","videos\\spy2_3.mkv"]]

  popular={"Spy X Family Part1":["photos\\spy1.png"," Genres:Action,Comedy\n Status:Completed\n Ep total:3"],
          "Demon Slayer":["photos\\slayer.png"," Genres:Action,Fantasy\n Status:Completed\n Ep total:3"],
          "Naruto Shippuden":["photos\\naruto.png"," Genres:Action,Adventure\n Status:Completed\n Ep total:3"]
          }
  topAiring={"One Piece":["photos\\one.png"," Genres:Action,Fantasy\n Status:Ongoing\n Ep total:3"],
             "Blue Lock":["photos\\blue.png"," Genres:Sports,Shounen\n Status:Ongoing\n Ep total:3"],
             "Spy X Family Part 2":["photos\\spy2.png"," Genres:Action,Comedy\n Status:Ongoing\n Ep total:3"]
            }
 
  canvas.pack(fill='both',expand = True)
  canvas.create_image(0,0,image=background_photo,anchor='nw')
  canvas.create_text(320,30,text="ANIME-STREAMING",font=("Helvetica",25),fill='white')
  
  popularLabel.place(x=5,y=60)    
  j=120
  popularPI=[]
  for i in popular:
   popularPI.append(PhotoImage(file=popular[i][0]))
  for i in popularPI:
    canvas.create_image(j,180,image=i)
    j=j+200
  j=120
  k=0
  btnList=[]
  count=0
  for i in popular:
    btnList.append(Button(canvas,text="PLAY",bg="green",borderwidth=3,command=partial(Play,i,popular[i][1],v1[count])))
    canvas.create_window(j,273,window=btnList[k])
    j=j+200
    k=k+1
    count=count+1
  
  
  topAiringLabel.place(x=5,y=300)
  j=120
  topAiringPI=[]
  for i in topAiring:
   topAiringPI.append(PhotoImage(file=topAiring[i][0]))
  for i in topAiringPI:
    canvas.create_image(j,419,image=i)
    j=j+200 
  j=120
  k=0
  btnList2=[]
  count=0
  for i in topAiring:
    btnList2.append(Button(canvas,text="PLAY",bg="green",borderwidth=3,command=partial(Play,i,topAiring[i][1],v2[count])))
    canvas.create_window(j,515,window=btnList2[k])
    j=j+200
    k=k+1
    count=count+1




  
  window.mainloop()
 
 
 


 
 
'''
sImage=Image.open('photos\\onepiecepng')
re2=sImage.resize((150,150)) #150 150 
re2.save("photos\\one.png")
'''
 
startImage=PhotoImage(file='photos\\startimg.png')
welcomeText=Label (window,text="Welcome to Anime Streaming application",
                 font=('Arial',23,'bold'),
                 fg="green",
                 bg='black',
                 relief=RAISED,
                 bd=15,
                 padx=15,
                 pady=10,
                 image=startImage,
                 compound='bottom'
                 )
welcomeText.pack()
 
button= Button(window,text='Click to Continue...',
              command=click,
              font=("Comic Sans",18),
              bg="#00FF00",
              fg="black",
              )                
button.pack()

   
window.mainloop()
