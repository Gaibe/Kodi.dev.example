import sys
import xbmc
import xbmcgui

selectHeading       = 'Choose your test'
testList            = ['browse','browsemultiple','browsesingle','input',
                        'multiselect','notification','numeric','ok',
                        'textviewer','yesno']

def chooseYourTest():
    while True:
        testChosen = xbmcgui.Dialog().select(selectHeading, testList)
        if testChosen < 0:
            break
        elif testList[testChosen] == 'browse':
            testBrowse()
        elif testList[testChosen] == 'browsemultiple':
            testBrowseMultiple()
        elif testList[testChosen] == 'browsesingle':
            testBrowseSingle()
        elif testList[testChosen] == 'input':
            testInput()
        elif testList[testChosen] == 'multiselect':
            testMultiSelect()
        elif testList[testChosen] == 'notification':
            testNotification()
        elif testList[testChosen] == 'numeric':
            testNumeric()
        elif testList[testChosen] == 'ok':
            testOk()
        elif testList[testChosen] == 'textviewer':
            testTextViewer()
        elif testList[testChosen] == 'yesno':
            testYesNo()

# type : integer - the type of browse dialog.
#     - 0 : ShowAndGetDirectory
#     - 1 : ShowAndGetFile
#     - 2 : ShowAndGetImage
#     - 3 : ShowAndGetWriteableDirectory
# heading : string or unicode - dialog heading.
# shares : string or unicode - from sources.xml. (i.e. 'myprograms')
# mask : [optional] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
# useThumbs : [optional] boolean - if True autoswitch to Thumb view if files exist.
# treatAsFolder : [optional] boolean - if True playlists and archives act as folders.
# defaultt : [optional] string - default path or file.
# enableMultiple : [optional] boolean - if True multiple file selection is enabled. Is ignored if type is 0 or 3
# RETURN If enableMultiple is False (default): returns filename and/or path as a string
#           to the location of the highlighted item, or default value if canceled.
#       If enableMultiple is True: returns tuple of marked filenames as a string, or empty tuple if canceled
# SINCE (at least) 12.X Frodo
def testBrowse():
    xbmcgui.Dialog().browse(type=2,heading='Test browse',shares='files',
            mask='.png|.jpg|.jpeg|.gif',useThumbs=True,treatAsFolder=False,
            defaultt='special://',enableMultiple=True)

# type : integer - the type of browse dialog.
#     - 1 : ShowAndGetFile
#     - 2 : ShowAndGetImage
# heading : string or unicode - dialog heading.
# shares : string or unicode - from sources.xml. (i.e. 'myprograms')
# mask : [optional] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
# useThumbs : [optional] boolean - if True autoswitch to Thumb view if files exist (default=false).
# treatAsFolder : [optional] boolean - if True playlists and archives act as folders (default=false).
# defaultt : [optional] string - default path or file.
# RETURN tuple of marked filenames as a string, or empty tuple if canceled
# SINCE 13.X Gotham
def testBrowseMultiple():
    xbmcgui.Dialog().browseMultiple(type=1,heading='Test browsemultiple',
            shares='myprograms',useThumbs=True,defaultt='addons://sources/executable')

# type : integer - the type of browse dialog.
#    - 0 : ShowAndGetDirectory
#    - 1 : ShowAndGetFile
#    - 2 : ShowAndGetImage
#    - 3 : ShowAndGetWriteableDirectory
# heading : string or unicode - dialog heading.
# shares : string or unicode - from sources.xml. (i.e. 'myprograms')
# mask : [optional] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
# useThumbs : [optional] boolean - if True autoswitch to Thumb view if files exist (default=False).
# treatAsFolder : [optional] boolean - if True playlists and archives act as folders (default=False).
# defaultt : [optional] string - default path or file.
# RETURN filename and/or path as a string to the location of the highlighted item, or default value if canceled 
# SINCE 13.X Gotham
def testBrowseSingle():
    xbmcgui.Dialog().browseSingle(type=1,heading='Test browsesingle',shares='files',
            mask='.jpg|.pdf|.txt',treatAsFolder=False,
            defaultt='special://masterprofile/script_data/XBMC Lyrics')

# heading : string - dialog heading.
# defaultt : [optional] string - default value. (default=empty string) 
# type : [optional] integer - the type of keyboard dialog. (default=xbmcgui.INPUT_ALPHANUM) 
#     - xbmcgui.INPUT_ALPHANUM (standard keyboard)
#     - xbmcgui.INPUT_NUMERIC (format: #)
#     - xbmcgui.INPUT_DATE (format: DD/MM/YYYY)
#     - xbmcgui.INPUT_TIME (format: HH:MM)
#     - xbmcgui.INPUT_IPADDRESS (format: #.#.#.#)
#     - xbmcgui.INPUT_PASSWORD (return md5 hash of input, input is masked) 
# option : [optional] integer - option for the dialog.
#     - xbmcgui.PASSWORD_VERIFY (verifies an existing (default) md5 hashed password) for type xbmcgui.INPUT_PASSWORD
#     - xbmcgui.ALPHANUM_HIDE_INPUT (masks input) for type xbmcgui.INPUT_ALPHANUM
# autoclose : [optional] integer - milliseconds to autoclose dialog. (default=do not autoclose)
# RETURN the entered data as a string, or an empty string if canceled
# SINCE 13.X Gotham
def testInput():
    xbmcgui.Dialog().input(heading='Test input',defaultt='12:10',type=xbmcgui.INPUT_TIME,autoclose=0)

# heading : string or unicode - dialog heading.
# options : list of string - options to choose from.
# autoclose : [optional] integer - milliseconds to autoclose dialog. (default=do not autoclose)
# RETURN the selected items as a list of indices, or None if cancelled
# SINCE 16.X Jarvis
def testMultiSelect():
    xbmcgui.Dialog().multiselect(heading='Test multiselect',
            options=['Select 1', 'Select 2', 'Select 3', 'Choose me !'],autoclose=10000)

# heading : string - dialog heading.
# message : string - dialog message.
# icon : [optional] string - icon to use. (default xbmcgui.NOTIFICATION_INFO)
#   - xbmcgui.NOTIFICATION_INFO
#   - xbmcgui.NOTIFICATION_WARNING
#   - xbmcgui.NOTIFICATION_ERROR
# time : [optional] integer - time in milliseconds (default 5000)
# sound : [optional] bool - play notification sound (default True)
# SINCE 15.X Isengard
def testNotification():
    xbmcgui.Dialog().notification(heading='Test notification',message='Here is your notification message',
            icon=xbmcgui.NOTIFICATION_WARNING,time=6000,sound=False)

# type : integer - the type of numeric dialog.
#   - 0 : ShowAndGetNumber (default format: #)
#   - 1 : ShowAndGetDate (default format: DD/MM/YYYY)
#   - 2 : ShowAndGetTime (default format: HH:MM)
#   - 3 : ShowAndGetIPAddress (default format: #.#.#.#)
# heading : string or unicode - dialog heading.
# defaultt : [optional] string - default value.
# RETURN the entered value as a string (return default value if dialog is canceled)
# SINCE (at least) 12.X Frodo
def testNumeric():
    xbmcgui.Dialog().numeric(type=0,heading='Test numeric',defaultt='42')

# heading : string or unicode - dialog heading.
# line1 : string or unicode - line #1 multi-line text.
# line2 : [optional] string or unicode - line #2 text.
# line3 : [optional] string or unicode - line #3 text.
# RETURN True if 'Ok' was pressed, else False
# SINCE (at least) 12.X Frodo
def testOk():
    xbmcgui.Dialog().ok(heading='Test ok',line1='First line of text',line2='Second line of text',line3='Third line of text')

# heading : string or unicode - dialog heading.
# list : string list - list of items.
# autoclose : [optional] integer - milliseconds to autoclose dialog. (default=do not autoclose)
# RETURN the position of the highlighted item as an integer (return 1 for "option1")
# SINCE (at least) 12.X Frodo
def testSelect():
    xbmcgui.Dialog().select(heading='Test select',list=['option1', 'option2', 'option3'],autoclose=0)

# heading : string or unicode - dialog heading.
# text : string or unicode - text.
# SINCE 16.X Jarvis
def testTextViewer():
    xbmcgui.Dialog().textviewer(heading='Test textviewer',text='Some random text')

# heading : string or unicode - dialog heading.
# line1 : string or unicode - line #1 multi-line text.
# line2 : [optional] string or unicode - line #2 text.
# line3 : [optional] string or unicode - line #3 text.
# nolabel : [optional] label to put on the no button.
# yeslabel : [optional] label to put on the yes button.
# autoclose : [optional] integer - milliseconds to autoclose dialog. (default=do not autoclose)
# RETURN True if 'Yes' was pressed, else False
# SINCE (at least) 12.X Frodo
def testYesNo():
    xbmcgui.Dialog().yesno(heading='Test yesno',line1='First line',line2='Second line',line3='Third line',
            nolabel='nop',yeslabel='why not',autoclose=0)

### Start of script
if (__name__ == '__main__'):
    chooseYourTest()