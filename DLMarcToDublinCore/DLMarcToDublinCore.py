
from pymarc import MARCReader  #import pymarc for marc21 handling 
import re   #import re - the Python system commands library 
import os   # read records in marc file .mrc
import shutil # for ziping files

#configuration need to be changed 
open_path = 'C:\\Users\\hkixxx\\Desktop\\KFNL Dlibrary\\DLAddItems\\DLFilesMissingBibItemItyp2.mrc'
out_path = 'C:\\Users\\hkixxx\\Desktop\\KFNL Dlibrary\\DLAddItems\\KFNL\\00_Data_files\\'

# variables value 
xml_start   = '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<dublin_core schema="dc">\n'
xml_001     = '<dcvalue element="identifier" qualifier="dbid">'
xml_006     = '<dcvalue element="source" qualifier="frequency">'
xml_008     = '<dcvalue element="language" qualifier="iso">'
xml_008_17  = '<dcvalue element="publisher" qualifier="country">'
xml_008_22  = '<dcvalue element="rights" qualifier="audience">'
xml_010     = '<dcvalue element="identifier" qualifier="lccn">'
xml_020     = '<dcvalue element="identifier" qualifier="isbn">'
xml_022     = '<dcvalue element="identifier" qualifier="issn">'
xml_035     = '<dcvalue element="identifier" qualifier="oclc">'
xml_050     = '<dcvalue element="identifier" qualifier="lc">'
xml_082     = '<dcvalue element="identifier" qualifier="ddc">'
xml_090     = '<dcvalue element="identifier" qualifier="callnum">'
xml_100     = '<dcvalue element="contributor" qualifier="author">'
xml_110     = '<dcvalue element="contributor" qualifier="corporate">'
xml_111     = '<dcvalue element="contributor" qualifier="meeting">'
xml_245     = '<dcvalue element="title" qualifier="">'
xml_246     = '<dcvalue element="title" qualifier="alternative">'
xml_250     = '<dcvalue element="source" qualifier="edition">'
xml_260a    = '<dcvalue element="publisher" qualifier="city">'
xml_260b    = '<dcvalue element="publisher" qualifier="">'
xml_260c    = '<dcvalue element="date" qualifier="issued">'
xml_260m    = '<dcvalue element="date" qualifier="issuedhijri">'
xml_300     = '<dcvalue element="description" qualifier="extent">'
xml_490     = '<dcvalue element="relation" qualifier="ispartof">'
xml_500     = '<dcvalue element="description" qualifier="">'
xml_502     = '<dcvalue element="description" qualifier="theses">'
xml_504     = '<dcvalue element="description" qualifier="bib">'
xml_505     = '<dcvalue element="description" qualifier="toc">'
xml_520     = '<dcvalue element="description" qualifier="abstract">'
xml_536     = '<dcvalue element="description" qualifier="">'
xml_650     = '<dcvalue element="subject" qualifier="isi">'
xml_856     = '<dcvalue element="identifier" qualifier="uri">'
xml_949i    = '<dcvalue element="type" qualifier="format">'
xml_fld     = '</dcvalue>\n'
xml_end     = '<dcvalue element="rights" qualifier="digital">no</dcvalue>\n<dcvalue element="rights" qualifier="digitized">yes</dcvalue>\n<dcvalue element="rights" qualifier="hold">yes</dcvalue>\n</dublin_core>\n'

#remove folder  
if os.path.exists(out_path):
    shutil.rmtree(out_path)

# make data folder 
os.mkdir(out_path)
# begining of the DC record and metadata values 
Num = 100
with open(open_path, 'rb') as fh:
  reader = MARCReader(fh)
  
  for record in reader:
    # write record dublin core
    xml_record = xml_start
    # tag 001
    if record['001'] is not None:
        t001 =  re.sub('[^0-9]*','', record['001'].format_field())
        xml_record = xml_record + xml_001 + t001 + xml_fld
    else:
        t001 = 'N'+str(Num)
        xml_record = xml_record + xml_001 + t001 + xml_fld
    #need work 
    if record['006'] is not None :
        t006 = record['006'].format_field()[1]
        xml_record = xml_record + xml_006 + t006 + xml_fld
    else:
        t006 = 'None'
    
    if record['008'] is not None and len(str(record['008'])) == 46:
        #100929s2011  maua   b  001 0 eng 
        t008_17 = record['008'].format_field()[15:17]
        xml_record = xml_record + xml_008_17 + t008_17 + xml_fld

        t008_22 = record['008'].format_field()[22]
        xml_record = xml_record + xml_008_22 + t008_22 + xml_fld
        
        if record['008'].format_field()[35:38] == 'eng':
            t008 = 'انجليزي'

        elif record['008'].format_field()[35:38] == 'ara':
             t008 = 'عربي'

        elif record['008'].format_field()[35:38] == 'fre':
             t008 = 'فرنسي'

        elif record['008'].format_field()[35:38] == 'ind':
             t008 = 'اندونيسي'

        elif record['008'].format_field()[35:38] == 'ben':
             t008 = 'بنغالي'

        elif record['008'].format_field()[35:38] == 'urd':
             t008 = 'اردو'

        elif record['008'].format_field()[35:38] == 'hau':
             t008 = 'الهوسا'   

        elif record['008'].format_field()[35:38] == 'tag':
             t008 = 'تغالوغ'
        
        elif record['008'].format_field()[35:38] == 'ita':
             t008 = 'ايطالي'
        else:
            t008 = record['008'].format_field()[35:38]
        
        xml_record = xml_record + xml_008 + t008 + xml_fld
    else:
        t008 = 'None'

    #tag 010
    if record['010'] is not None:
        t010 = xml_010 + record['010'].format_field() + xml_fld
        xml_record = xml_record + t010
    else:
        t010 = 'None'
    
    #tag 020
    if record['020'] and record['020']['a'] is not None:
        t020 = xml_020 + str(record['020']['a']) + xml_fld
        xml_record = xml_record + t020
    else:
        t020 = 'None'

    #tag 022
    if record['022'] and record['022']['a'] is not None:
        t022 = xml_022 + record['022']['a'] + xml_fld
        xml_record = xml_record + t022
    else:
        t022 = 'None'

    #tag 035
    if record['035'] and record['035']['a'] is not None:
        t035 = xml_035 + record['035'].format_field() + xml_fld
        xml_record = xml_record + t035
    else:
        t035 = 'None'
    
    #tag 050
    if record['050'] is not None:
        t050 = xml_050 + record['050'].format_field() + xml_fld
        xml_record = xml_record + t050
    else:
        t050 = 'None'

    # tag 082
    if record['082'] and record['082']['a'] is not None:
        t082 = xml_082 + re.sub('None', '',str(record['082']['a'])+str(record['082']['b'])) + xml_fld
        xml_record = xml_record + t082
    else:
        t082 = 'None'

    #tag 090
    if record['090'] and record['090']['a'] is not None:
        t090 = xml_090 + re.sub('None', '',str(record['090']['a'])+str(record['090']['b']))+ xml_fld
        xml_record = xml_record + t090  
    else:
        t090 = 'None'

    # tag 100
    
    if record['100'] and record['100']['a'] is not None:
        t100 = xml_100 + re.sub('None', '',str(record['100']['a'])+str(record['100']['d'])) + xml_fld
        xml_record = xml_record + t100    
    else:
        t100 = 'None'
    
    # tag 110
    if record['110'] and record['110']['a'] is not None:
        t110 = xml_110 + record['110']['a'] + xml_fld
        xml_record = xml_record + t110        
    else:
        t110 = 'None'

    if record['111'] and record['111']['a'] is not None:
        t111 = xml_111 + record['111']['a'] + xml_fld
        xml_record = xml_record + t111    
    else:
        t111 = 'None'

    if record['130'] and record['130']['a'] is not None:
        t130 = xml_246 + record['130'].format_field() + xml_fld
        xml_record = xml_record + t130    
    else:
        t130 = 'None'
    
    if record['222'] is not None:
        t222 = xml_245 + re.sub('\/$|//$','', record.title()) + xml_fld
        xml_record = xml_record + t222
    else:
        t222 = 'None'
    

    if record['245'] is not None:
        t245 = xml_245 + re.sub('\/$|//$','', str(record.title())) + xml_fld
        xml_record = xml_record + t245
    else:
        t245 = 'None'
    
    if record['246'] is not None:
        t246 = xml_246 + re.sub('\/$|//$','', record.title()) + xml_fld
        xml_record = xml_record + t246
    else:
        t246 = 'None'

    if record['210'] is not None:
        t210 = xml_246 + record['210']['a'] + ' ' + record['210']['b'] + xml_fld
        xml_record = xml_record + t210
    else:
        t210 = 'None'
    
    if record['240'] is not None:
        t240 = xml_246 + record['240']['a'] + xml_fld
        xml_record = xml_record + t240
    else:
        t240 = 'None'

    if record['740'] is not None:
        t740 = xml_246 + record['740']['a'] + xml_fld
        xml_record = xml_record + t740
    else:
        t240 = 'None'

    if record['250'] and record['250']['a'] is not None:
        t250 = xml_250 + record['250'].format_field() + xml_fld
        xml_record = xml_record + t250
    else:
        t250 = 'None'

    for pub_location in record.get_fields('260'):
        if record['260'] and record['260']['a'] is not None:
            t260a = xml_260a + re.sub(' [;|:]','',record['260']['a']) + xml_fld
            xml_record = xml_record + t260a
        else:
            t260a = 'None'
    for publisher in record.get_fields('260'):
        if record['260'] and record['260']['b'] is not None:
            t260b = xml_260b + re.sub(',| ,|،| ،','',record.publisher()) + xml_fld
            xml_record = xml_record + t260b
        else:
            t260b = 'None'

    if record['260'] and record['260']['m'] is not None:
        t260c = xml_260c + re.sub('[^0-9]','',str(record['260']['m'])) + xml_fld
        xml_record = xml_record + t260c
    else:
        t260c = 'None'
    
    if record['260'] and record['260']['c'] is not None:
        t260m = xml_260m + record['260']['c'] + xml_fld
        xml_record = xml_record + t260m
    else:
        t260c = 'None'

    if record['264'] and record['264']['a'] is not None:
        t264a = xml_260a + re.sub(' [;|:]','',record['264']['a']) + xml_fld
        xml_record = xml_record + t264a
    else:
        t264a = 'None'
    
    if record['264'] and record['264']['b'] is not None:
        t264b = xml_260b + re.sub(',| ,| ،|،','',record['264']['b']) + xml_fld
        xml_record = xml_record + t264b     
    else:
        t264b = 'None'

    if record['264'] and record['264']['c'] is not None:
        t264c = xml_260c + re.sub('[^0-9]','',record['264']['c']) + xml_fld
        xml_record = xml_record + t264c
    else:
        t264c = 'None'

    if record['300'] is not None:
        t300 = xml_300 + record['300'].format_field() + xml_fld
        xml_record = xml_record + t300
    else:
        t300 = 'None'
  
    for series in record.get_fields('440','490'):
         t490 = xml_490 + series.format_field() + xml_fld
         xml_record = xml_record + t490

    if record['500'] is not None:
        t500 = xml_500 + record['500'].format_field() + xml_fld
        xml_record = xml_record + t500
    else:
        t500 = 'None'
    
    if record['502'] is not None:
        t502 = xml_502 + record['502'].format_field() + xml_fld
        xml_record = xml_record + t502
    else:
        t502 = 'None'
    
    if record['504'] is not None:
        t504 = xml_504 + record['504'].format_field() + xml_fld
        xml_record = xml_record + t504
    else:
        t502 = 'None'

    if record['505'] is not None:
        t505 = xml_505 + record['505'].format_field() + xml_fld
        xml_record = xml_record + t505
    else:
        t505 = 'None'

    if record['520'] is not None:
        txt = record['520'].format_field()
        txt = txt.replace('<','&lt;')
        txt = txt.replace('>','&gt;')
        txt = txt.replace('&','&amp;')
        t520 = xml_520 + txt + xml_fld
        xml_record = xml_record + t520
    else:
        t520 = 'None'
    
    if record['536'] is not None:

        t536 = xml_536 + record['536'].format_field() + xml_fld
        xml_record = xml_record + t536
    else:
        t520 = 'None'
    #supject = record.get_fields('600','650','651','600')
    for supject in record.get_fields('600','610','630','650','651','653','676','690'):
         t650 = re.sub('=6..  ..\$a', '',str(supject))
         t650 = re.sub('\$2.*','', t650)
         t650 = xml_650 + re.sub('\$.|\/', ' - ', t650) + xml_fld
         xml_record = xml_record + t650
    for person in record.get_fields('700'):
        if record['700'] is not None:
            t700 = xml_100 + str(record['700']['a']) + str(record['700']['d']) + xml_fld
            xml_record = xml_record + t700
        else:
            t700 = 'None'

    if record['710'] and record['710']['a'] is not None:
        t710 = xml_110 + record['710']['a'] + xml_fld
        xml_record = xml_record + t710
    else:
       t710 = 'None'

    if record['711'] and record['711']['a'] is not None:
        t711 = xml_111 + record['711']['a'] + xml_fld
        xml_record = xml_record + t711
    else:
       t711 = 'None'

    if record['800'] and record['800']['a'] is not None:
        t800 = xml_100 + re.sub('None', '',str(record['800']['a'])+str(record['800']['d'])) + xml_fld
        xml_record = xml_record + t800
    else:
        t800 = 'None'
    
    if record['810'] and record['810']['a'] is not None:
        t810 = xml_110 + record['810']['a'] + xml_fld
        xml_record = xml_record + t810
    else:
       t810 = 'None'

    if record['811'] and record['811']['a'] is not None:
        t811 = xml_111 + record['811']['a'] + xml_fld
        xml_record = xml_record + t811
    else:
       t811 = 'None'

    if record['856'] and record['856']['u'] is not None:
        t856 = xml_856 + record['856']['u'] + xml_fld
        xml_record = xml_record + t856
    else:
       t856 = 'None'

    #please add all item types
    if record['949'] and record['949']['i'] is not None:
        if record['949']['i'] == 'ك' or record['949']['i'] == 'B':
            t949_value='كتاب'
        elif record['949']['i'] =='D':
            t949_value='رسالة جامعية'
        elif record['949']['i'] =='ر س د':
            t949_value='دكتواره'
        elif record['949']['i'] =='ر س م':
            t949_value='ماجستير'
        else:
            t949_value = record['949']['i']

        t949i = xml_949i + t949_value + xml_fld
        xml_record = xml_record + t949i
    else:
       t949i = 'None'
    
    # replace any spacial character inside the DC files 
    xml_record = re.sub('œ', '', xml_record)
    xml_record = re.sub('&', '&amp;', xml_record)
    xml_record = re.sub('/‎', '', xml_record)
    xml_record = re.sub('<<|>>' , '--', xml_record)
    xml_record = re.sub(' <', '<', xml_record)
    xml_record = re.sub('> ', '>', xml_record)
    xml_record = re.sub('  ', ' ', xml_record)
    xml_record = re.sub('؛<|-<|\.<|:<|،<|None<', '<', xml_record)
    xml_record = re.sub(' <', '<', xml_record)
    xml_record = re.sub('.*"></dcvalue>\n', '', xml_record)
    
    xml_record = xml_record + xml_end
    os.mkdir(out_path+'{0}'.format(t001))
    out_f = open(out_path+'{0}\\dublin_core.xml'.format(t001), '+a' ,encoding='UTF-8')
    out_f.write (xml_record)
    out_f.close()
       
    # #end of program