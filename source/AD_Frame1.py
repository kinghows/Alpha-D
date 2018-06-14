#Boa:Frame:Frame1

import wx
import wx.richtext
import wx.gizmos
import os
import subprocess
import re
import xml.etree.ElementTree as ET  
import sys
import random
import time
from PIL import Image
import math
import hashlib
import urllib
import urllib2
import base64
import json

SCREENSHOT_WAY = 3

def setParams(array, key, value):
    array[key] = value
    
def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, urllib.quote(str(parser[key]), safe = ''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str)
    return hash_md5.hexdigest().upper()
    
def pull_screenshot():
    global SCREENSHOT_WAY
    if 1 <= SCREENSHOT_WAY <= 3:
        process = subprocess.Popen(
            'adb shell screencap -p',
            shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
        elif SCREENSHOT_WAY == 1:
            binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
        f = open('dy.png', 'wb')
        f.write(binary_screenshot)
        f.close()
    elif SCREENSHOT_WAY == 0:
        os.system('adb shell screencap -p /sdcard/dy.png')
        os.system('adb pull /sdcard/dy.png .')

def check_screenshot():
    global SCREENSHOT_WAY
    if os.path.isfile('dy.png'):
        try:
            os.remove('dy.png')
        except Exception:
            pass
    if SCREENSHOT_WAY < 0:
        return 0
    pull_screenshot()
    try:
        Image.open('./dy.png').load()
    except Exception:
        SCREENSHOT_WAY -= 1
        check_screenshot()
    return 1
        

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1APP_ID, wxID_FRAME1APP_KEY, wxID_FRAME1BEAUTY, 
 wxID_FRAME1BTN_CLEAR, wxID_FRAME1BTN_FOLLOW, wxID_FRAME1BTN_MOBILE, 
 wxID_FRAME1BTN_NEXT, wxID_FRAME1BTN_STAR, wxID_FRAME1BTN_START, 
 wxID_FRAME1BTN_TEST_BEAUTY, wxID_FRAME1FOLLOW_X, wxID_FRAME1FOLLOW_Y, 
 wxID_FRAME1GENERICDIRCTRL1, wxID_FRAME1NEXT_X, wxID_FRAME1NEXT_Y, 
 wxID_FRAME1PANEL1, wxID_FRAME1RADIOBUTTON1, wxID_FRAME1RADIOBUTTON2, 
 wxID_FRAME1SASHLAYOUTWINDOW1, wxID_FRAME1STAR_X, wxID_FRAME1STAR_Y, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TEXTRETURN, 
] = [wx.NewId() for _init_ctrls in range(29)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(438, 55), size=wx.Size(873, 704),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Alpha-D')
        self.SetClientSize(wx.Size(857, 665))
        self.Bind(wx.EVT_SIZE, self.OnFrame1Size)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(392, -8), size=wx.Size(463, 664),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetMinSize(wx.Size(455, 778))

        self.sashLayoutWindow1 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(392, 664), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow1.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow1.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow1.SetDefaultSize(wx.Size(392, 664))
        self.sashLayoutWindow1.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashLayoutWindow1SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW1)

        self.textReturn = wx.TextCtrl(id=wxID_FRAME1TEXTRETURN,
              name=u'textReturn', parent=self.panel1, pos=wx.Point(104, 8),
              size=wx.Size(1110, 1050), style=wx.TE_MULTILINE, value='')

        self.btn_start = wx.Button(id=wxID_FRAME1BTN_START,
              label=u'\u5f00\u59cb', name=u'btn_start', parent=self.panel1,
              pos=wx.Point(16, 144), size=wx.Size(75, 24), style=0)
        self.btn_start.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BTN_START)

        self.genericDirCtrl1 = wx.GenericDirCtrl(defaultFilter=0, dir='.',
              filter=u'Fichier png(*.png,*.jpg)|*.png;*.jpg',
              id=wxID_FRAME1GENERICDIRCTRL1, name='genericDirCtrl1',
              parent=self.sashLayoutWindow1, pos=wx.Point(0, 0),
              size=wx.Size(392, 664),
              style=wx.DIRCTRL_3D_INTERNAL | wx.SUNKEN_BORDER)
        self.genericDirCtrl1.SetMinSize(wx.Size(270, 664))
        self.genericDirCtrl1.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSel)

        self.btn_mobile = wx.Button(id=wxID_FRAME1BTN_MOBILE,
              label=u'\u5f53\u524d\u8bbe\u5907', name=u'btn_mobile',
              parent=self.panel1, pos=wx.Point(16, 240), size=wx.Size(75, 24),
              style=0)
        self.btn_mobile.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BTN_MOBILE)

        self.btn_clear = wx.Button(id=wxID_FRAME1BTN_CLEAR,
              label=u'\u6e05\u7a7a\u7ed3\u679c', name=u'btn_clear',
              parent=self.panel1, pos=wx.Point(16, 288), size=wx.Size(75, 24),
              style=0)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BTN_CLEAR)

        self.beauty = wx.TextCtrl(id=wxID_FRAME1BEAUTY, name=u'beauty',
              parent=self.panel1, pos=wx.Point(48, 16), size=wx.Size(48, 22),
              style=0, value=u'80')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'\u989c\u503c>', name='staticText1', parent=self.panel1,
              pos=wx.Point(8, 16), size=wx.Size(33, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'\u6027\u522b\uff1a', name='staticText2',
              parent=self.panel1, pos=wx.Point(8, 56), size=wx.Size(36, 14),
              style=0)

        self.radioButton1 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON1,
              label=u'\u7537', name='radioButton1', parent=self.panel1,
              pos=wx.Point(72, 56), size=wx.Size(32, 16), style=0)
        self.radioButton1.SetValue(True)
        self.radioButton1.Enable(True)
        self.radioButton1.Show(True)
        self.radioButton1.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButton1Radiobutton, id=wxID_FRAME1RADIOBUTTON1)

        self.radioButton2 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON2,
              label=u'\u5973', name='radioButton2', parent=self.panel1,
              pos=wx.Point(40, 56), size=wx.Size(32, 14), style=0)
        self.radioButton2.SetValue(True)
        self.radioButton2.Bind(wx.EVT_RADIOBUTTON,
              self.OnRadioButton2Radiobutton, id=wxID_FRAME1RADIOBUTTON2)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(48, 88), size=wx.Size(48, 22),
              style=0, value=u'10')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'\u5148\u5237\uff1a', name='staticText3',
              parent=self.panel1, pos=wx.Point(8, 88), size=wx.Size(36, 14),
              style=0)

        self.btn_test_beauty = wx.Button(id=wxID_FRAME1BTN_TEST_BEAUTY,
              label=u'\u989c\u503c\u68c0\u6d4b', name=u'btn_test_beauty',
              parent=self.panel1, pos=wx.Point(16, 192), size=wx.Size(75, 24),
              style=0)
        self.btn_test_beauty.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BTN_TEST_BEAUTY)

        self.app_key = wx.TextCtrl(id=wxID_FRAME1APP_KEY, name=u'app_key',
              parent=self.panel1, pos=wx.Point(0, 632), size=wx.Size(104, 22),
              style=0, value=u'ecTptvOyErjHiNgo')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'app_key\uff1a', name='staticText4', parent=self.panel1,
              pos=wx.Point(0, 616), size=wx.Size(58, 14), style=0)

        self.app_id = wx.TextCtrl(id=wxID_FRAME1APP_ID, name=u'app_id',
              parent=self.panel1, pos=wx.Point(0, 592), size=wx.Size(104, 22),
              style=0, value=u'1106941552')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'app_id\uff1a', name='staticText5', parent=self.panel1,
              pos=wx.Point(0, 576), size=wx.Size(48, 14), style=0)

        self.star_y = wx.TextCtrl(id=wxID_FRAME1STAR_Y, name=u'star_y',
              parent=self.panel1, pos=wx.Point(56, 520), size=wx.Size(40, 24),
              style=0, value=u'960')

        self.star_x = wx.TextCtrl(id=wxID_FRAME1STAR_X, name=u'star_x',
              parent=self.panel1, pos=wx.Point(8, 520), size=wx.Size(40, 24),
              style=0, value=u'987')

        self.btn_star = wx.Button(id=wxID_FRAME1BTN_STAR, label=u'\u70b9\u8d5e',
              name=u'btn_star', parent=self.panel1, pos=wx.Point(16, 552),
              size=wx.Size(75, 24), style=0)
        self.btn_star.Bind(wx.EVT_BUTTON, self.OnBtn_starButton,
              id=wxID_FRAME1BTN_STAR)

        self.btn_follow = wx.Button(id=wxID_FRAME1BTN_FOLLOW,
              label=u'\u5173\u6ce8', name=u'btn_follow', parent=self.panel1,
              pos=wx.Point(16, 488), size=wx.Size(75, 24), style=0)
        self.btn_follow.Bind(wx.EVT_BUTTON, self.OnBtn_followButton,
              id=wxID_FRAME1BTN_FOLLOW)

        self.btn_next = wx.Button(id=wxID_FRAME1BTN_NEXT, label=u'\u7ffb\u9875',
              name=u'btn_next', parent=self.panel1, pos=wx.Point(16, 424),
              size=wx.Size(75, 24), style=0)
        self.btn_next.Bind(wx.EVT_BUTTON, self.OnBtn_nextButton,
              id=wxID_FRAME1BTN_NEXT)

        self.follow_x = wx.TextCtrl(id=wxID_FRAME1FOLLOW_X, name=u'follow_x',
              parent=self.panel1, pos=wx.Point(8, 456), size=wx.Size(40, 22),
              style=0, value=u'987')

        self.follow_y = wx.TextCtrl(id=wxID_FRAME1FOLLOW_Y, name=u'follow_y',
              parent=self.panel1, pos=wx.Point(56, 456), size=wx.Size(40, 22),
              style=0, value=u'796')

        self.next_x = wx.TextCtrl(id=wxID_FRAME1NEXT_X, name=u'next_x',
              parent=self.panel1, pos=wx.Point(8, 392), size=wx.Size(40, 24),
              style=0, value=u'540')

        self.next_y = wx.TextCtrl(id=wxID_FRAME1NEXT_Y, name=u'next_y',
              parent=self.panel1, pos=wx.Point(56, 392), size=wx.Size(40, 22),
              style=0, value=u'965')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.FileName=None
        self.gender =0
        self.config ={"center_point":{"x": 540,"y": 965,"rx": 10,"ry": 300},"follow_bottom":{"x": 987,"y": 796,"rx": 10,"ry": 10},"star_bottom":{"x": 987,"y": 960,"rx": 10,"ry": 10}}
        try:      
            if check_screenshot():
                cmd = "adb shell wm size"  
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
                p=p[p.find('Override size:')+15:].strip()
                if len(p)>0 :
                    self.textReturn.AppendText('Screensize: '+  p +'\n')
                else:
                    self.textReturn.AppendText('not connect! '+'\n') 
            else:
                self.textReturn.AppendText('not connect! '+'\n') 
        except Exception:
            self.textReturn.AppendText('not connect! '+'\n')

    def checkStatusRange(self, event):
        return event.GetDragStatus() != wx.SASH_STATUS_OUT_OF_RANGE

    def doLayout(self):
        wx.LayoutAlgorithm().LayoutWindow(self, self.panel1)
        self.panel1.Refresh()
        

    def adb_shell(self, cmd):
        cmd ='adb shell '+cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_code = p.poll()    
        while return_code is None:
            line = p.stdout.readline()
            return_code = p.poll()
            line = line.strip()
            if line:
                self.textReturn.AppendText(line+'\n')

    def OnWxframe1Size(self, event):
        self.doLayout()

    def OnSashLayoutWindow1SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow1.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()
        event.Skip()

    def OnSashLayoutWindow2SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow2.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()
        event.Skip()

    def OnFrame1Size(self, event):
        self.doLayout()
        event.Skip()

        
    def OnSel(self, event):
        self.FileName = self.genericDirCtrl1.GetFilePath()
   
            
    def next_page(self):
        cmd = 'input swipe {x1} {y1} {x2} {y2} {duration}'.format(
            x1=int(self.next_x.Value),
            y1=int(self.next_y.Value)+300,
            x2=int(self.next_x.Value),
            y2=int(self.next_y.Value),
            duration=200
        )
        self.adb_shell(cmd)
        time.sleep(1.5)

    def follow_user(self):
        cmd = 'input tap {x} {y}'.format(
            x=int(self.follow_x.Value) + random.randint(-10,10),
            y=int(self.follow_y.Value) + random.randint(-10,10)
        )
        self.adb_shell(cmd)
        time.sleep(0.5)


    def thumbs_up(self):
        cmd = 'input tap {x} {y}'.format(
            x=int(self.star_x.Value) + random.randint(-10,10),
            y=int(self.star_y.Value) + random.randint(-10,10)
        )
        self.adb_shell(cmd)
        time.sleep(0.5)
        
    def OnBtn_starButton(self, event):
        self.thumbs_up()
        event.Skip()

    def OnBtn_followButton(self, event):
        self.follow_user()
        event.Skip()

    def OnBtn_nextButton(self, event):
        self.next_page()
        event.Skip()
        
    def OnButton2Button(self, event):
        n = 1
        while n <=int(self.textCtrl2.Value.encode("ascii")):
            pull_screenshot()
                        
            self.resize_image('dy.png', 'optimized.png', 1024*1024)

            with open('optimized.png', 'rb') as bin_data:
                image_data = bin_data.read()

            str_rsp = self.face_detectface(image_data,0)
            dict_rsp = json.loads(str_rsp)
            
            if dict_rsp['ret'] == 0:
                beauty = 0
                for face in dict_rsp['data']['face_list']:
                    face_area = (face['x'], face['y'], face['x']+face['width'], face['y']+face['height'])
                img = Image.open("optimized.png")
                cropped_img = img.crop(face_area).convert('RGB')
                cropped_img.save('./face/'+str(face['gender'])+'_'+str(face['beauty'])+'_'+str(face['face_id'])+'.png')
                self.textReturn.AppendText(str(n)+':\n')
                self.textReturn.AppendText('face_id: '+ str(face['face_id'])+'\n')
                self.textReturn.AppendText('gender: '+ str(face['gender'])+'\n')
                self.textReturn.AppendText('beauty: '+ str(face['beauty'])+'\n')
                self.textReturn.AppendText('age: '+ str(face['age'])+'\n')
                self.textReturn.AppendText('expression: '+ str(face['expression'])+'\n')
                if face['beauty'] > beauty :
                    if self.gender==0 and face['gender'] < 50:
                        beauty = face['beauty']
                    elif self.gender==1 and face['gender'] > 50:
                        beauty = face['beauty']

                if beauty >= int(self.beauty.Value):
                    self.thumbs_up()
                    self.follow_user()
                    self.textReturn.AppendText('Focus a beauty!'+'\n')
                else:
                    self.textReturn.AppendText('Pass!'+'\n')
            else:
                self.textReturn.AppendText(str(dict_rsp['msg'])+'\n')
                
            n += 1
            self.next_page()
            time.sleep(1)

        event.Skip()
        
    def OnButton5Button(self, event):
        size_str = os.popen('adb shell wm size').read()
        device_str = os.popen('adb shell getprop ro.product.model').read()
        density_str = os.popen('adb shell wm density').read()
        self.textReturn.AppendText(device_str+'\n')
        self.textReturn.AppendText(size_str+'\n')
        self.textReturn.AppendText(density_str+'\n')
        event.Skip()

    def OnButton6Button(self, event):
        self.textReturn.Clear()
        event.Skip()

    def OnRadioButton1Radiobutton(self, event):
        self.gender =1
        event.Skip()

    def OnRadioButton2Radiobutton(self, event):
        self.gender =0
        event.Skip()

    def invoke(self, params):
        self.url_data = urllib.urlencode(params)
        req = urllib2.Request(self.url, self.url_data)
        try:
            rsp = urllib2.urlopen(req)
            str_rsp = rsp.read()
            return str_rsp
        except Exception as e:
            self.textReturn.AppendText(e+'\n')
            return {'ret': -1}
          
    def face_detectface(self, image, mode):
        self.url = 'https://api.ai.qq.com/fcgi-bin/face/face_detectface'
        self.data = {}
        setParams(self.data, 'app_id', self.app_id.Value)
        setParams(self.data, 'app_key', self.app_key.Value)
        setParams(self.data, 'mode', mode)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data.decode("utf-8"))
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)
    
    def resize_image(self, origin_img, optimize_img, threshold):
        with Image.open(origin_img) as im:
            width, height = im.size
            file_size =  width*height
            if file_size > threshold:
 
                if width >= height:
                    new_width = int(math.sqrt(threshold / 2))
                    new_height = int(new_width * height * 1.0 / width)
                else:
                    new_height = int(math.sqrt(threshold / 2))
                    new_width = int(new_height * width * 1.0 / height)

                resized_im = im.resize((new_width, new_height))
                resized_im.save(optimize_img)
            else:
                im.save(optimize_img)    
            
    def OnButton1Button(self, event):
        if os.path.isfile(self.FileName):
            self.textReturn.AppendText(self.FileName+'\n')
            
            self.resize_image(self.FileName, 'optimized.png', 1024*1024)
            
            with open('optimized.png', 'rb') as bin_data:
                image_data = bin_data.read()
            
            str_rsp = self.face_detectface(image_data,0)
            dict_rsp = json.loads(str_rsp)
            #file = open("e:\json.txt","w")
            #file.write(str_rsp)
            #file.close()
            
            if dict_rsp['ret'] == 0:
                for face in dict_rsp['data']['face_list']:
                    face_area = (face['x'], face['y'], face['x']+face['width'], face['y']+face['height'])
                img = Image.open('optimized.png')
                cropped_img = img.crop(face_area).convert('RGB')
                cropped_img.save('./face/'+str(face['gender'])+'_'+str(face['beauty'])+'_'+str(face['face_id'])+'.png')
                self.textReturn.AppendText('face_id: '+ str(face['face_id'])+'\n')
                self.textReturn.AppendText('gender: '+ str(face['gender'])+'\n')
                self.textReturn.AppendText('beauty: '+ str(face['beauty'])+'\n')
                self.textReturn.AppendText('age: '+ str(face['age'])+'\n')
                self.textReturn.AppendText('expression: '+ str(face['expression'])+'\n')
            else:
                self.textReturn.AppendText(str(dict_rsp['msg'])+'\n')
        event.Skip()


