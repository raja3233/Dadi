from Tkinter import *

class Game:

    player1left=11
    player2left=11
    player1kills=0
    player2kills=0
    initialx=0
    initialy=0
    finalx=0
    finaly=0
    horizontalDadiPositions=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23]]
    verticalDadiPositions=[[0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]]
    redCoinsPosition=[]
    blueCoinsPositions=[]
    draw=False
    dadi=False
    hasCoin={'top_top_left':False,'top_top_middle':False,'top_top_right':False,
            'top_middle_left':False,'top_middle_middle':False,'top_middle_right':False,
             'top_bottom_left':False,'top_bottom_middle':False,'top_bottom_right':False,
             'middle_left_left':False,'middle_left_middle':False,'middle_left_right':False,
             'middle_right_left':False,'middle_right_middle':False,'middle_right_right':False,
             'bottom_top_left':False,'bottom_top_middle':False,'bottom_top_right':False,
            'bottom_middle_left':False,'bottom_middle_middle':False,'bottom_middle_right':False,
             'bottom_bottom_left':False,'bottom_bottom_middle':False,'bottom_bottom_right':False
             }
    coinAtPosition={'top_top_left':False,'top_top_middle':False,'top_top_right':False,
            'top_middle_left':False,'top_middle_middle':False,'top_middle_right':False,
             'top_bottom_left':False,'top_bottom_middle':False,'top_bottom_right':False,
             'middle_left_left':False,'middle_left_middle':False,'middle_left_right':False,
             'middle_right_left':False,'middle_right_middle':False,'middle_right_right':False,
             'bottom_top_left':False,'bottom_top_middle':False,'bottom_top_right':False,
            'bottom_middle_left':False,'bottom_middle_middle':False,'bottom_middle_right':False,
             'bottom_bottom_left':False,'bottom_bottom_middle':False,'bottom_bottom_right':False
             }
    playerChance='Player1'
    #initialing the window
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x700')
        self.root.resizable(width=False,height=False)
        self.root.wm_title("DadiGame")

    #creating statring frame for the user details
    def setupFrame(self):

        self.frame=Frame(self.root,width=300,heigh=200,bg="gray")
        self.frame.pack(fill=BOTH,padx=50,pady=100)
        self.msg=Label(self.frame,text='Enter player Details',bg='gray')
        self.msg.place(relx=.5,rely=.2,anchor='c')
        label1=Label(self.frame,text='Player1',bg='gray',fg='red' ,font='60')
        label1.place(relx=.3,rely=.4,anchor='c')
        label2=Label(self.frame,text='Player2',bg='gray',fg='red',font='60')
        label2.place(relx=.3,rely=.6,anchor='c')
        button=Button(self.frame,text="StartGame",command=self.loadGame)
        button.place(relx=0.5,rely=.9,anchor="c")
        button.configure(bg='dark green',fg='white')
        self.entry1=Entry(self.frame,bd=2)
        self.entry1.place(relx=.5,rely=.4,anchor='c')
        self.entry2=Entry(self.frame,bd=2)
        self.entry2.place(relx=.5,rely=.6,anchor='c')



    #loads the game provided valid player names

    def loadGame(self):


        self.player1=self.entry1.get().strip()
        self.player2=self.entry2.get().strip()

        if self.player1=="" or self.player2=="":

            self.msg.configure(text='Please enter both player names')
        else:
            self.frame.place_forget()
            self.frame.destroy()
            self.loadNewGame()




    def loadNewGame(self):


        #creating lable for displaying messages
        self.msgLabel=Label(self.root,text='NextMove:'+self.player1,fg='green')
        self.msgLabel.place(relx=.5,rely=.1,anchor='c')
        #creating  players place
        self.create_players_place()
        #creating board
        board=Frame(self.root,width=500,height=500)
        board.place(rely=.5,relx=.5,anchor='c')
        self.canvas=Canvas(board,width=500,height=500)
        self.canvas.pack(fill=BOTH)
        self.canvas.bind('<Button-1>',self.initialClickPositions)
        self.canvas.bind('<B1-Motion>',self.finalPositions)
        #creating outer circles
        self.canvas.create_rectangle(10,10,495,495)
        self.canvas.create_rectangle(95,95,400,400)
        self.canvas.create_rectangle(170,170,330,330)
        #creating lines
        self.canvas.create_line(10,250,170,250)
        self.canvas.create_line(250,10,250,170)
        self.canvas.create_line(250,330,250,495)
        self.canvas.create_line(330,250,495,250)
        #creating circles
        self.create_circles()

    def finalPositions(self,event):
        self.finalx=event.x
        self.finaly=event.y


    def initialClickPositions(self,event):
        self.initialx=event.x
        self.initialy=event.y
        self.finalx=event.x
        self.finaly=event.y

    def create_players_place(self):
        player_frame1=Frame(self.root,width=100,height=100,bg='gray')
        player_frame1.place(relx=0.1,rely=0.5,anchor='c')
        player1Label=Label(player_frame1,text=self.player1,fg='red')
        player1Label.pack(side=TOP,fill=BOTH)
        self.player1_kills_label=Label(player_frame1,text="kills:0")
        self.player1_left_label=Label(player_frame1,text="left:11")
        self.player1_kills_label.pack(side=TOP,fill=BOTH)
        self.player1_left_label.pack(side=BOTTOM,fill=BOTH)
        player_frame2=Frame(self.root,width=100,height=100,bg='gray')
        player_frame2.place(relx=0.9,rely=0.5,anchor='c')
        player2Label=Label(player_frame2,text=self.player2,fg='blue')
        player2Label.pack(side=TOP,fill=BOTH)
        self.player2_kills_label=Label(player_frame2,text="kills:0")
        self.player2_left_label=Label(player_frame2,text="left:11")
        self.player2_kills_label.pack(side=TOP,fill=BOTH)
        self.player2_left_label.pack(side=BOTTOM,fill=BOTH)

    def create_circles(self):
        self.top_top_left=self.canvas.create_circle(15,15,10,fill='white',tags='top_top_left')
        self.canvas.tag_bind(self.top_top_left,'<ButtonRelease-1>',lambda x:self.updateBoard('top_top_left'))
        self.top_top_middle=self.canvas.create_circle(250,15,10,fill='white',tags='top_top_middle')
        self.canvas.tag_bind(self.top_top_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('top_top_middle'))
        self.top_top_right=self.canvas.create_circle(490,15,10,fill='white',tags='top_top_right')
        self.canvas.tag_bind(self.top_top_right,'<ButtonRelease-1>',lambda x:self.updateBoard('top_top_right'))
        self.top_middle_left=self.canvas.create_circle(95,95,10,fill='white',tags='top_middle_left')
        self.canvas.tag_bind(self.top_middle_left,'<ButtonRelease-1>',lambda x:self.updateBoard('top_middle_left'))
        self.top_middle_middle=self.canvas.create_circle(250,95,10,fill='white',tags='top_middle_middle')
        self.canvas.tag_bind(self.top_middle_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('top_middle_middle'))
        self.top_middle_right=self.canvas.create_circle(400,95,10,fill='white',tags='top_middle_right')
        self.canvas.tag_bind(self.top_middle_right,'<ButtonRelease-1>',lambda x:self.updateBoard('top_middle_right'))
        self.top_bottom_left=self.canvas.create_circle(170,170,10,fill='white',tags='top_bottom_left')
        self.canvas.tag_bind(self.top_bottom_left,'<ButtonRelease-1>',lambda x:self.updateBoard('top_bottom_left'))
        self.top_bottom_middle=self.canvas.create_circle(250,170,10,fill='white',tags='top_bottom_middle')
        self.canvas.tag_bind(self.top_bottom_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('top_bottom_middle'))
        self.top_bottom_right=self.canvas.create_circle(330,170,10,fill='white',tags='top_bottom_right')
        self.canvas.tag_bind(self.top_bottom_right,'<ButtonRelease-1>',lambda x:self.updateBoard('top_bottom_right'))
        self.middle_left_left=self.canvas.create_circle(15,250,10,fill='white',tags='middle_left_left')
        self.canvas.tag_bind(self.middle_left_left,'<ButtonRelease-1>',lambda x:self.updateBoard('middle_left_left'))
        self.middle_left_middle=self.canvas.create_circle(95,250,10,fill='white',tags='middle_left_middle')
        self.canvas.tag_bind(self.middle_left_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('middle_left_middle'))
        self.middle_left_right=self.canvas.create_circle(170,250,10,fill='white',tags='middle_left_right')
        self.canvas.tag_bind(self.middle_left_right,'<ButtonRelease-1>',lambda x:self.updateBoard('middle_left_right'))
        self.middle_right_left=self.canvas.create_circle(330,250,10,fill='white',tags='middle_right_left')
        self.canvas.tag_bind(self.middle_right_left,'<ButtonRelease-1>',lambda x:self.updateBoard('middle_right_left'))
        self.middle_right_middle=self.canvas.create_circle(400,250,10,fill='white',tags='middle_right_middle')
        self.canvas.tag_bind(self.middle_right_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('middle_right_middle'))
        self.middle_right_right=self.canvas.create_circle(490,250,10,fill='white',tags='middle_right_right')
        self.canvas.tag_bind(self.middle_right_right,'<ButtonRelease-1>',lambda x:self.updateBoard('middle_right_right'))
        self.bottom_top_left=self.canvas.create_circle(170,330,10,fill='white',tags='bottom_top_left')
        self.canvas.tag_bind(self.bottom_top_left,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_top_left'))
        self.bottom_top_middle=self.canvas.create_circle(250,330,10,fill='white',tags='bottom_top_middle')
        self.canvas.tag_bind(self.bottom_top_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_top_middle'))
        self.bottom_top_right=self.canvas.create_circle(330,330,10,fill='white',tags='bottom_top_right')
        self.canvas.tag_bind(self.bottom_top_right,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_top_right'))
        self.bottom_middle_left=self.canvas.create_circle(95,400,10,fill='white',tags='bottom_middle_left')
        self.canvas.tag_bind(self.bottom_middle_left,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_middle_left'))
        self.bottom_middle_middle=self.canvas.create_circle(250,400,10,fill='white',tags='bottom_middle_middle')
        self.canvas.tag_bind(self.bottom_middle_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_middle_middle'))
        self.bottom_middle_right=self.canvas.create_circle(400,400,10,fill='white',tags='bottom_middle_right')
        self.canvas.tag_bind(self.bottom_middle_right,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_middle_right'))
        self.bottom_bottom_middle=self.canvas.create_circle(250,490,10,fill='white',tags='bottom_bottom_middle')
        self.canvas.tag_bind(self.bottom_bottom_middle,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_bottom_middle'))
        self.bottom_middle_left=self.canvas.create_circle(15,490,10,fill='white',tags='bottom_bottom_left')
        self.canvas.tag_bind(self.bottom_middle_left,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_bottom_left'))
        self.bottom_bottom_right=self.canvas.create_circle(490,490,10,fill='white',tags='bottom_bottom_right')
        self.canvas.tag_bind(self.bottom_bottom_right,'<ButtonRelease-1>',lambda x:self.updateBoard('bottom_bottom_right'))


    def determinePlace(self,x,y,r=10):

            if self.oncircle(x,y,15,15,r):
                return 'top_top_left'
            elif self.oncircle(x,y,250,15,r):
                return 'top_top_middle'
            elif self.oncircle(x,y,490,15,r):
                return 'top_top_right'
            elif self.oncircle(x,y,95,95,r):
                return 'top_middle_left'
            elif self.oncircle(x,y,250,95,r):
                return 'top_middle_middle'
            elif self.oncircle(x,y,400,95,r):
                return 'top_middle_right'
            elif self.oncircle(x,y,170,170,r):
                return 'top_bottom_left'
            elif self.oncircle(x,y,250,170,r):
                return 'top_bottom_middle'
            elif self.oncircle(x,y,330,170,r):
                return 'top_bottom_right'
            elif self.oncircle(x,y,15,250,r):
                return 'middle_left_left'
            elif self.oncircle(x,y,95,250,r):
                return 'middle_left_middle'
            elif self.oncircle(x,y,170,250,r):
                return 'middle_left_right'
            elif self.oncircle(x,y,330,250,r):
                return 'middle_right_left'
            elif self.oncircle(x,y,400,250,r):
                return 'middle_right_middle'
            elif self.oncircle(x,y,490,250,r):
                return 'middle_right_right'
            elif self.oncircle(x,y,170,330,r):
                return 'bottom_top_left'
            elif self.oncircle(x,y,250,330,r):
                return 'bottom_top_middle'
            elif self.oncircle(x,y,330,330,r):
                return 'bottom_top_right'
            elif self.oncircle(x,y,95,400,r):
                return 'bottom_middle_left'
            elif self.oncircle(x,y,250,400,r):
                return 'bottom_middle_middle'
            elif self.oncircle(x,y,400,400,r):
                return 'bottom_middle_right'
            elif self.oncircle(x,y,250,490,r):
                return 'bottom_bottom_middle'
            elif self.oncircle(x,y,15,490,r):
                return 'bottom_bottom_left'
            elif self.oncircle(x,y,490,490,r):
                return 'bottom_bottom_right'
            else:
                return -1






    def oncircle(self,x,y,x1,y1,r):
        if (x-x1)**2+(y-y1)**2<=r**2:
            return True
        else:
            return False


    def updateBoard(self,place):

        if self.dadi==True:
            dadiCoinSelected=self.isDadiCoinSelected(place)
            if not dadiCoinSelected and self.hasCoin[place]:

                if self.playerChance=='Player1' and self.coinAtPosition[place]=='blue':
                    self.canvas.itemconfig(place,fill='white')
                    self.hasCoin[place]=False
                    self.coinAtPosition[place]=False
                    self.dadi=False
                    self.playerChance='Player2'
                    self.player1kills+=1
                    if(self.player1kills==11):
                        self.msgLabel.configure(text=self.player1+' won',fg='pink')
                        return
                    self.blueCoinsPositions.remove(self.getPosition(place))
                    self.player1_kills_label.configure(text="kills:"+str(self.player1kills))
                    self.msgLabel.configure(text='NextMove:'+self.player2)
                elif self.playerChance=='Player2' and self.coinAtPosition[place]=='red':
                    self.canvas.itemconfig(place,fill='white')
                    self.hasCoin[place]=False
                    self.coinAtPosition[place]=False
                    self.dadi=False
                    self.playerChance='Player1'
                    self.player2kills+=1
                    if(self.player2kills==11):
                        self.msgLabel.configure(text=self.player2+' won',fg='pink')
                        return
                    self.redCoinsPosition.remove(self.getPosition(place))
                    self.player2_kills_label.configure(text="kills:"+str(self.player2kills))
                    self.msgLabel.configure(text='NextMove:'+self.player1)
                else:
                    self.msgLabel.configure(text='choose others player coin only')

            else:
                if dadiCoinSelected:
                    self.msgLabel.configure(text='choose non dadi coin')
                else:
                    self.msgLabel.configure(text='choose non other player coin')



        elif self.hasCoin[place] and (self.player1left>0 or self.player2left>0):
                self.msgLabel.configure(text='you can not place the coin' )
        elif self.hasMove(place):
            if self.playerChance=='Player1':
                if(self.player1left>0):
                    self.player1left-=1
                    self.canvas.itemconfig(place,fill='red')
                    self.hasCoin[place]=True
                    self.redCoinsPosition.append(self.getPosition(place))
                    self.coinAtPosition[place]='red'
                    self.player1_left_label.configure(text='left:'+str(self.player1left))
                    if(self.isDadi(place)):
                        self.dadi=True
                        self.msgLabel.configure(text='choose :'+self.player2+' '+' coin to remove')
                        self.playerChance='Player1'
                    else:
                        self.msgLabel.configure(text='NextMove:'+self.player2)
                        self.playerChance='Player2'
                else:
                    coinPositionToMove=self.determinePlace(self.initialx,self.initialy)
                    coinPositionToPlace=self.determinePlace(self.finalx,self.finaly)
                    if self.hasCoin[coinPositionToMove] and coinPositionToPlace!=-1 and not self.hasCoin[coinPositionToPlace]:
                        if self.isMovable(coinPositionToMove) and self.coinAtPosition[coinPositionToMove]=='red':
                            if coinPositionToPlace != coinPositionToMove:
                                self.canvas.itemconfig(coinPositionToPlace,fill='red')
                                self.hasCoin[coinPositionToPlace]=True
                                self.redCoinsPosition.append(self.getPosition(coinPositionToPlace))
                                self.coinAtPosition[coinPositionToPlace]='red'
                                self.canvas.itemconfig(coinPositionToMove,fill='white')
                                self.hasCoin[coinPositionToMove]=False
                                self.redCoinsPosition.remove(self.getPosition(coinPositionToMove))
                                self.coinAtPosition[coinPositionToMove]=False
                                print self.isDadi(coinPositionToPlace),':',coinPositionToPlace
                                if(self.isDadi(coinPositionToPlace)):
                                    self.dadi=True
                                    self.msgLabel.configure(text='choose :'+self.player2+' '+' coin to remove')
                                    self.playerChance='Player1'
                                else:
                                    self.msgLabel.configure(text='NextMove:'+self.player2)
                                    self.playerChance='Player2'
                            else:
                                self.msgLabel.configure(text=self.player1+"choose different position to place")
                                self.playerChance='Player1'


                        else:
                            self.msgLabel.configure(text="It is not movable. "+self.player1+" choose movable coin")
                            self.playerChance='Player1'

                    else:
                        if coinPositionToPlace==-1:
                            self.msgLabel.configure(text=self.player1+" drag the coin to circle")
                            self.playerChance='Player1'
                        else:
                            self.msgLabel.configure(text=self.player1+" select and drag the coin to move")
                            self.playerChance='Player1'



            elif self.playerChance=='Player2':
                if(self.player2left>0):
                    self.player2left-=1
                    self.canvas.itemconfig(place,fill='blue')
                    self.hasCoin[place]=True
                    self.blueCoinsPositions.append(self.getPosition(place))
                    self.coinAtPosition[place]='blue'
                    self.player2_left_label.configure(text='left:'+str(self.player2left))
                    if(self.isDadi(place)):
                        self.dadi=True
                        self.msgLabel.configure(text='choose :'+self.player1+' '+' coin to remove')
                        self.playerChance='Player2'
                    else:
                        self.msgLabel.configure(text='NextMove:'+self.player1)
                        self.playerChance='Player1'
                else:
                    coinPositionToMove=self.determinePlace(self.initialx,self.initialy)
                    coinPositionToPlace=self.determinePlace(self.finalx,self.finaly)
                    print coinPositionToPlace,":",coinPositionToMove
                    if self.hasCoin[coinPositionToMove] and coinPositionToPlace!=-1 and not self.hasCoin[coinPositionToPlace]:
                        if self.isMovable(coinPositionToMove) and self.coinAtPosition[coinPositionToMove]=='blue':
                            if coinPositionToPlace != coinPositionToMove:
                                self.canvas.itemconfig(coinPositionToPlace,fill='blue')
                                self.hasCoin[coinPositionToPlace]=True
                                self.blueCoinsPositions.append(self.getPosition(coinPositionToPlace))
                                self.coinAtPosition[coinPositionToPlace]='blue'
                                self.canvas.itemconfig(coinPositionToMove,fill='white')
                                self.blueCoinsPositions.remove(self.getPosition(coinPositionToMove))
                                self.hasCoin[coinPositionToMove]=False
                                self.coinAtPosition[coinPositionToMove]=False
                                print self.isDadi(coinPositionToPlace) ,':',coinPositionToPlace
                                if(self.isDadi(coinPositionToPlace)):
                                    self.dadi=True
                                    self.msgLabel.configure(text='choose :'+self.player1+' '+' coin to remove')
                                    self.playerChance='Player2'
                                else:
                                    self.msgLabel.configure(text='NextMove:'+self.player1)
                                    self.playerChance='Player1'
                            else:
                                self.msgLabel.configure(text=self.player2+"choose different position to place")
                                self.playerChance='Player2'


                        else:
                            self.msgLabel.configure(text="It is not movable. "+self.player2+"choose movable coin")
                            self.playerChance='Player2'

                    else:
                        if coinPositionToPlace==-1:
                            self.msgLabel.configure(text=self.player2+" drag the coin to circle")
                            self.playerChance='Player2'
                        else:
                            self.msgLabel.configure(text=self.player2+" select and drag the coin to move")
                            self.playerChance='Player2'
        else:
            if(self.draw):
                winner='both'
            elif(self.player1kills>self.player2kills):
                winner="player1"
            elif(self.player1kills<self.player2kills):
                winner='player2'
            else:
                winner='both'
            self.msgLabel.configure(text='Game won by'+winner,fg='orange')

    def isDadiCoinSelected(self,place):
        return (self.checkHorizontally(place) or self.checkVertically(place))


    def getPosition(self,value):
            if(value=='top_top_left'):
                return 0
            if value=='top_top_middle':
                return 1
            if value=='top_top_right':
                return 2
            if value=='top_middle_left':
                return 3
            if value=='top_middle_middle':
                return 4
            if value=='top_middle_right':
                return 5
            if value=='top_bottom_left':
                return 6
            if value=='top_bottom_middle':
                return 7
            if value=='top_bottom_right':
                return 8
            if value=='middle_left_left':
                return 9
            if value=='middle_left_middle':
                return 10
            if value=='middle_left_right':
                return 11
            if value=='middle_right_left':
                return 12
            if value=='middle_right_middle':
                return 13
            if value=='middle_right_right':
                return 14
            if value=='bottom_top_left':
                return 15
            if value=='bottom_top_middle':
                return 16
            if value=='bottom_top_right':
                return 17
            if value=='bottom_middle_left':
                return 18
            if value=='bottom_middle_middle':
                return 19
            if value=='bottom_middle_right':
                return 20
            if value=='bottom_bottom_left':
                return 21
            if value=='bottom_bottom_middle':
                return 22
            if value=='bottom_bottom_right':
                return 23



    def isDadi(self,place):
        return (self.checkHorizontally(place) or self.checkVertically(place) )


    def checkVertically(self,place):
        print self.coinAtPosition[place]
        for verticalDadiPosition in self.verticalDadiPositions:
            if (self.coinAtPosition[place]=='red'):
                print self.getPosition(place),':',verticalDadiPosition,':',self.getPosition(place) in verticalDadiPosition
                if self.getPosition(place) in verticalDadiPosition:
                    print verticalDadiPosition,':',self.redCoinsPosition,':',self.sublistExist(verticalDadiPosition,self.redCoinsPosition)
                    if (self.sublistExist(verticalDadiPosition,self.redCoinsPosition)):
                        return True
            elif (self.coinAtPosition[place]=='blue'):
                print self.getPosition(place),':',verticalDadiPosition,':',self.getPosition(place) in verticalDadiPosition
                if self.getPosition(place) in verticalDadiPosition:
                    print verticalDadiPosition,':',self.blueCoinsPositions,':',self.sublistExist(verticalDadiPosition,self.blueCoinsPositions)
                    if (self.sublistExist(verticalDadiPosition,self.blueCoinsPositions)):
                        return True

        return False

    def checkHorizontally(self,place):
        print self.coinAtPosition[place]
        for horizontalDadiPosition in self.horizontalDadiPositions:
            if (self.coinAtPosition[place]=='red'):
                print self.getPosition(place),':',horizontalDadiPosition,':',self.getPosition(place) in horizontalDadiPosition
                if self.getPosition(place) in horizontalDadiPosition:
                    if (self.sublistExist(horizontalDadiPosition,self.redCoinsPosition)):
                        return True
            elif (self.coinAtPosition[place]=='blue'):
                print self.getPosition(place),':',horizontalDadiPosition,':',self.getPosition(place) in horizontalDadiPosition
                if self.getPosition(place) in horizontalDadiPosition:
                    if (self.sublistExist(horizontalDadiPosition,self.blueCoinsPositions)):
                        return True
        else:
            return False

    def sublistExist(self,sublist,mainlist):
        for i in sublist:
            if i not in mainlist:
                return False
        return True

    def hasMove(self,place):

        if self.playerChance=='Player1':
           if self.player1left>0 :
                return True
           else:
               if self.player2kills==11:
                   return False
               elif self.deadMoveFor('player1'):
                    return False
               else:
                   return True

        elif self.playerChance=='Player2':
           if self.player2left>0:
                return True
           else:
               if self.player2kills==11:
                   return False
               elif self.deadMoveFor('player2'):
                    return False
               else:
                   return True

    def deadMoveFor(self,player):
        if(player=='player1'):
            for place,coin in self.coinAtPosition.iteritems():
                if(coin=='red'):
                    if self.isMovable(place):
                        return False
            self.draw=True
            return True
        elif(player=='player2'):
            for place,coin in self.coinAtPosition.iteritems():
                if(coin=='blue'):
                    if self.isMovable(place):
                        return False
            self.draw=True
            return True

    def isMovable(self,place):

        if(place=='top_top_left'):
            if((not self.hasCoin['middle_left_left']) or (not self.hasCoin['top_top_middle'])):
                return True
        if(place=='top_middle_left'):
            if((not self.hasCoin['middle_left_middle']) or (not self.hasCoin['top_middle_middle'])):
                return True

        if(place=='top_bottom_left'):
            if((not self.hasCoin['middle_left_right']) or (not self.hasCoin['top_bottom_middle'])):
                return True
        if(place=='top_top_right'):
            if((not self.hasCoin['middle_right_right']) or (not self.hasCoin['top_top_middle'])):
                return True
        if(place=='top_middle_right'):
            if((not self.hasCoin['middle_right_middle']) or (not self.hasCoin['top_middle_middle'])):
                return True

        if(place=='top_bottom_right'):
            if((not self.hasCoin['middle_right_left']) or (not self.hasCoin['top_bottom_middle'])):
                return True
        if(place=='bottom_top_left'):
            if((not self.hasCoin['middle_left_right']) or (not self.hasCoin['bottom_top_middle'])):
                return True
        if(place=='bottom_middle_left'):
            if((not self.hasCoin['middle_left_middle']) or (not self.hasCoin['bottom_middle_middle'])):
                return True

        if(place=='bottom_bottom_left'):
            if((not self.hasCoin['middle_left_left']) or (not self.hasCoin['bottom_bottom_middle'])):
                return True
        if(place=='bottom_top_right'):
            if((not self.hasCoin['middle_right_left']) or (not self.hasCoin['bottom_top_middle'])):
                return True
        if(place=='bottom_middle_right'):
            if((not self.hasCoin['middle_right_middle']) or (not self.hasCoin['bottom_middle_middle'])):
                return True

        if(place=='bottom_bottom_right'):
            if((not self.hasCoin['middle_right_right']) or (not self.hasCoin['bottom_bottom_middle'])):
                return True
        if(place=='top_top_middle'):
            if((not self.hasCoin['top_top_left']) or (not self.hasCoin['top_top_right']) or (not self.hasCoin['top_middle_middle']) ):
                return True
        if(place=='top_middle_middle'):
            if((not self.hasCoin['top_middle_left']) or (not self.hasCoin['top_middle_right']) or (not self.hasCoin['top_top_middle']) or (not self.hasCoin['top_bottom_middle'])):
                return True
        if(place=='top_bottom_middle'):
            if((not self.hasCoin['top_bottom_left']) or (not self.hasCoin['top_bottom_right']) or (not self.hasCoin['top_middle_middle'])):
                return True
        if(place=='bottom_top_middle'):
            if((not self.hasCoin['bottom_top_left']) or (not self.hasCoin['bottom_top_right']) or (not self.hasCoin['bottom_middle_middle'])):
                return True
        if(place=='bottom_middle_middle'):
            if((not self.hasCoin['bottom_middle_left']) or (not self.hasCoin['bottom_middle_right']) or (not self.hasCoin['bottom_top_middle']) or (not self.hasCoin['bottom_bottom_middle'])):
                return True
        if(place=='bottom_bottom_middle'):
            if((not self.hasCoin['bottom_bottom_left']) or (not self.hasCoin['bottom_bottom_right']) or (not self.hasCoin['bottom_middle_middle'])):
                return True
        if(place=='middle_left_left'):
            if((not self.hasCoin['bottom_bottom_left']) or (not self.hasCoin['top_top_left']) or (not self.hasCoin['middle_left_middle'])):
                return True
        if(place=='middle_left_middle'):
            if((not self.hasCoin['bottom_middle_left']) or (not self.hasCoin['top_middle_left']) or (not self.hasCoin['middle_left_left']) or (not self.hasCoin['middle_left_right']) ):
                return True
        if(place=='middle_left_right'):
            if((not self.hasCoin['bottom_top_left']) or (not self.hasCoin['top_bottom_left']) or (not self.hasCoin['middle_left_middle'])):
                return True
        if(place=='middle_right_left'):
            if((not self.hasCoin['bottom_top_right']) or (not self.hasCoin['top_bottom_right']) or (not self.hasCoin['middle_right_middle'])):
                return True
        if(place=='middle_right_middle'):
            if((not self.hasCoin['bottom_middle_right']) or (not self.hasCoin['top_middle_right']) or (not self.hasCoin['middle_right_left']) or (not self.hasCoin['middle_right_right'])):
                return True
        if(place=='middle_right_right'):
            if((not self.hasCoin['bottom_bottom_right']) or (not self.hasCoin['top_top_right']) or (not self.hasCoin['middle_right_middle'])):
                return True
        return False




#creating canvas circle method
def _create_cirle(self,x,y,r,**kwargs):
        return self.create_oval(x-r,y-r,x+r,y+r,**kwargs)

Canvas.create_circle=_create_cirle

gameBoard=Game()
gameBoard.setupFrame()
gameBoard.root.mainloop()



