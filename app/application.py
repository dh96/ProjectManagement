# coding: utf-8

# Demonstrator / keine Fehlerbehandlung

import cherrypy
import json
import ast
import datetime
from .database import Database_cl
from .view import View_cl
from .template import Template_cl

# Method-Dispatching!

# Übersicht Anforderungen / Methoden

global AngemeldeterMitarbeiter


#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   exposed = True # gilt für alle Methoden

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      # spezielle Initialisierung können hier eingetragen werden
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()

   #-------------------------------------------------------
   def getList_p(self, List):
   #-------------------------------------------------------
      return self.view_o.createList_px(List)

   #-------------------------------------------------------
   def getDetail_p(self, id_spl, List):
   #-------------------------------------------------------
      return self.view_o.createDetail_px(List)



class Projekt_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()

   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         "Data":'',
         "Rolle": None
      }
      if id == None:
         #data_a = self.db_o.ReadProjectData()
         retVal_o["Data"] = self.db_o.ReadProjectData()
         retVal_o["Rolle"] = globals()["AngemeldeterMitarbeiter"]
         #List = list(data_a.values())
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getList_p(List)
      else:
         retVal_o["Data"] = self.db_o.GetProjectData(id)
         retVal_o["Rolle"] = globals()["AngemeldeterMitarbeiter"]
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      print(data_opl)
      id = self.db_o.GetProjectMaxId()
      data_o = {
         'id': id,
         'Name': data_opl["Name"]
      }
      self.db_o.AddProject(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------
      print(data_opl)
      data_o = {
         'id': data_opl['id'],
         'Name': data_opl['Name']
      }
      self.db_o.UpdateProject(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteProject(id)
      return



class Komponente_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
      "Data":'',
      "Rolle":globals()['AngemeldeterMitarbeiter'],
      "Projekte": {
          'Projekt':None
      }
      }
      if id == None:
         retVal_o['Data'] = self.db_o.ReadComponentData()
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
         retVal_o['Projekte']['Projekt'] = self.db_o.ReadProjectData()
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getList_p(List)
      else:
         retVal_o['Data'] = self.db_o.GetComponentData(id)
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
         retVal_o['Projekte']['Projekt'] = self.db_o.ReadProjectData()
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      id = self.db_o.GetComponentMaxId()
      data_o = {
         'id': id,
         'Projekt': data_opl["Projekt"],
         'Komponente': data_opl["Komponente"]
      }
      self.db_o.AddComponent(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------
      data_o = {
         'id': data_opl['id'],
         'Projekt': data_opl["Projekt"],
         'Komponente': data_opl["Komponente"]
      }
      self.db_o.UpdateComponent(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteComponent(id)
      return

class ProjektKomponenten_cl(object):
   exposed = True
   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
      "Data":'',
      "Rolle":globals()['AngemeldeterMitarbeiter'],
      "Projekte": {
          'Projekt':None
         }
      }
      print(id)
      if id == '-1':
         retVal_o['Data'] = self.db_o.ReadComponentData()

      else:
         tmpPro = self.db_o.GetProjectData(id)
         tmpKomp = self.db_o.ReadComponentData()
         retVal_o['Data'] = {k:v for (k,v) in tmpKomp.items() if v['Projekt'] == tmpPro['Name']}

      retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
      retVal_o['Projekte']['Projekt'] = self.db_o.ReadProjectData()
      List = []
      List.append(retVal_o)
      retVal_s = self.app.getList_p(List)
      return retVal_s


class Mitarbeiter_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         'Data': {
            'SW':None,
            'QS':None,
            'Rolle':None
         }
      }

      retVal_o['Data']['SW'] = self.db_o.ReadEmployeeSWData()
      retVal_o['Data']['QS'] = self.db_o.ReadEmployeeQSData()
      retVal_o['Data']['Rolle'] = globals()['AngemeldeterMitarbeiter']
      List = []
      List.append(retVal_o)
      retVal_s = self.app.getList_p(List)
      return retVal_s


class MitarbeiterSW_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         data_a = self.db_o.ReadEmployeeSWData()
         List = list(data_a.values())
         retVal_s = self.app.getList_p(List)
      else:
         data_o = self.db_o.GetEmployeeSWData(id)
         List = []
         List.append(data_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      id = self.db_o.GetEmployeeSWMaxId()
      data_o = {
         'id': id,
         'Name': data_opl["Name"],
         'Vorname': data_opl["Vorname"],
         'Abteilung': data_opl["Abteilung"]
      }
      self.db_o.AddEmployeeSW(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------
      data_o = {
         'id': data_opl["id"],
         'Name': data_opl["Name"],
         'Vorname': data_opl["Vorname"],
         'Abteilung': data_opl["Abteilung"]
      }
      self.db_o.UpdateEmployeeSW(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteEmployeeSW(id)
      return

class MitarbeiterQS_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''

      if id == None:
         data_a = self.db_o.ReadEmployeeQSData()
         List = list(data_a.values())
         retVal_s = self.app.getList_p(List)
      else:
         data_o = self.db_o.GetEmployeeQSData(id)
         List = []
         List.append(data_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      id = self.db_o.GetEmployeeQSMaxId()
      data_o = {
         'id': id,
         'Name': data_opl["Name"],
         'Vorname': data_opl["Vorname"],
         'Abteilung': data_opl["Abteilung"]
      }
      self.db_o.AddEmployeeQS(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------
      data_o = {
         'id': data_opl["id"],
         'Name': data_opl["Name"],
         'Vorname': data_opl["Vorname"],
         'Abteilung': data_opl["Abteilung"]
      }
      self.db_o.UpdateEmployeeQS(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteEmployeeQS(id)
      return


class Kategorie_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         'Data': {
            'src':None,
            'src1':None,
            'Rolle': globals()['AngemeldeterMitarbeiter']
         }
      }
      retVal_o['Data']['src'] = self.db_o.ReadCatErrorData()
      retVal_o['Data']['src1'] = self.db_o.ReadCatCauseData()
      List = []
      List.append(retVal_o)
      retVal_s = self.app.getList_p(List)
      return retVal_s


class KategorieFehler_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         "Data":'',
         "Rolle":globals()['AngemeldeterMitarbeiter']
      }
      if id == None:
         retVal_o["Data"] = self.db_o.ReadCatErrorData()
         retVal_o["Rolle"] = globals()['AngemeldeterMitarbeiter']
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getList_p(List)
      else:

         retVal_o["Data"] = self.db_o.GetCatErrorData(id)
         retVal_o["Rolle"] = globals()['AngemeldeterMitarbeiter']
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      id = self.db_o.GetCatErrorMaxId()
      data_o = {
         'id': id,
         'Beschreibung': data_opl["Beschreibung"],
         'src': "Fehler"
      }
      self.db_o.AddCatError(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------
      data_o = {
         'id': data_opl["id"],
         'Beschreibung': data_opl["Beschreibung"],
         'src': "Fehler"
      }
      self.db_o.UpdateCatError(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteCatError(id)
      return

class KategorieUrsache_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()
   #-------------------------------------------------------
   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         "Data":None,
         "Rolle":globals()['AngemeldeterMitarbeiter']
      }

      if id == None:
         retVal_o["Data"] = self.db_o.ReadCatCauseData()
         retVal_o["Rolle"] = globals()['AngemeldeterMitarbeiter']
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getList_p(List)
      else:

         retVal_o["Data"] = self.db_o.GetCatCauseData(id)
         retVal_o["Rolle"] = globals()['AngemeldeterMitarbeiter']
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      id = self.db_o.GetCatCauseMaxId()
      data_o = {
         'id': id,
         'Beschreibung': data_opl["Beschreibung"],
         'src': "Ursache"
      }
      self.db_o.AddCatCause(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------
      data_o = {
         'id': data_opl["id"],
         'Beschreibung': data_opl["Beschreibung"],
         'src': "Ursache"
      }
      self.db_o.UpdateCatCause(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteCatCause(id)
      return

class FehlerErkannt_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()

   #-------------------------------------------------------
   def GET(self, id=None, data_opl=None):
   #-------------------------------------------------------

      retVal_s = ''
      retVal_o = {
         'Data':None,
         'Rolle': globals()['AngemeldeterMitarbeiter'],
         'reference':{
            'Komponenten':None,
            'Projekt':None,
            'Mitarbeiter':None,
            'KategorieFehler':None,
            'KategorieFehlerUrsache':None,
         }
      }
      if id == None or id == 'type=erkannt' or id == 'type=behoben':
         tmpData = self.db_o.ReadErrorData()
         if id == None:
            retVal_o['Data'] = tmpData
         elif id == 'type=erkannt':
            retVal_o['Data'] = {k:v for (k,v) in tmpData.items() if v['Status'] == 'Erkannt'}
            retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
            print(retVal_o['Rolle'])
         else:
            retVal_o['Data'] = {k:v for (k,v) in tmpData.items() if v['Status'] == 'Behoben'}
            retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']


         List = []
         List.append(retVal_o)
         retVal_s = self.app.getList_p(List)
      else:
         retVal_o['Data'] = self.db_o.GetErrorData(id)
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
         retVal_o['reference']['Mitarbeiter'] = self.db_o.ReadEmployeeSWData()
         retVal_o['reference']['Projekt'] = self.db_o.ReadProjectData()
         retVal_o['reference']['Komponenten'] = self.db_o.ReadComponentData()
         retVal_o['reference']['KategorieFehler'] = self.db_o.ReadCatErrorData()
         retVal_o['reference']['KategorieFehlerUrsache'] = self.db_o.ReadCatCauseData()
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
         print(retVal_o['Rolle'])
         List = []
         List.append(retVal_o)
         retVal_s = self.app.getDetail_p(id, List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      id = self.db_o.GetErrorMaxId()
      data_o = {
         'id': id,
         'Beschreibung': data_opl["Beschreibung"],
         'Mitarbeiter': data_opl["Mitarbeiter"],
         'Datum': data_opl["Datum"],
         'Komponente': data_opl["Komponente"],
         'Projekt': data_opl["Projekt"],
         'FehlerKategorie': data_opl["FehlerKategorie"],
         'Status': 'Erkannt',
         'BeschreibungFehlerUrsache': "",
         'MitarbeiterDerFehlerBehobenHat':"",
         'DatumDerBeseitigung':"",
         'KategorieFehlerUrsache':"",
         'Zustand':'erfasst'
      }
      self.db_o.AddError(data_o)
      return None

   #------------------------------------------------------
   def PUT(self, **data_opl):
   #------------------------------------------------------

      if data_opl['Zustand'] == "fehlgeschlagen":
         data_o = self.db_o.GetErrorData(data_opl["id"])
         print("unsuccessful")
         data_o['Status'] = 'Erkannt',
         data_o['Zustand'] = data_opl['Zustand']
         self.db_o.DeleteError(data_opl["id"])
      elif data_opl['Zustand'] == "erfolgreich":
         data_o = self.db_o.GetErrorData(data_opl["id"])
         data_o['Zustand'] = data_opl['Zustand']
         data_o['Status'] = 'Behoben'
         self.db_o.UpdateError(data_opl['id'], data_o)
      else:
         data_o = self.db_o.GetErrorData(data_opl["id"])
         data_o['Status'] = 'Behoben'
         data_o['BeschreibungFehlerUrsache'] = data_opl['BeschreibungFehlerUrsache']
         data_o['MitarbeiterDerFehlerBehobenHat'] = data_opl['MitarbeiterDerFehlerBehobenHat']
         data_o['DatumDerBeseitigung'] = data_opl['DatumDerBeseitigung']
         data_o['KategorieFehlerUrsache'] = data_opl['KategorieFehlerUrsache']
         data_o['Zustand'] = data_opl['Zustand']
         self.db_o.UpdateError(data_opl['id'], data_o)
      return None

   #-------------------------------------------------------
   def DELETE(self, id):
   #-------------------------------------------------------
      self.db_o.DeleteError(id)
      return

class AuswertungKat_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()

   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         'Data': [],
         'Rolle': globals()['AngemeldeterMitarbeiter']
         }
      if id == None:
         tempDataErr = self.db_o.ReadErrorData()
         for item in tempDataErr.values():
            retVal_o['Data'].append({'Beschreibung':item['Beschreibung'],'FehlerKategorie':item['FehlerKategorie'],'Status':item['Status']})
         retVal_o['Data'].sort(key=lambda x: x['FehlerKategorie'])
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']
      List = []
      List.append(retVal_o)
      retVal_s = self.app.getList_p(List)

      return retVal_s

class AuswertungPro_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()

   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         'Data': [],
         'Rolle': globals()['AngemeldeterMitarbeiter']
      }
      if id == None:
         tempDataErr = self.db_o.ReadErrorData()
         for item in tempDataErr.values():
            retVal_o['Data'].append({'Beschreibung':item['Beschreibung'],'Projekt':item['Projekt'],'Komponente':item['Komponente'],'Status':item['Status']})
         retVal_o['Data'].sort(key=lambda x: x['Projekt'])
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']

      List = []
      List.append(retVal_o)
      retVal_s = self.app.getList_p(List)
      print(retVal_s)
      return retVal_s


class AuswertungProZeit_cl(object):
   exposed = True
   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()

   def GET(self, id=None):
   #-------------------------------------------------------
      retVal_s = ''
      retVal_o = {
         'Data': [],
         'Rolle': globals()['AngemeldeterMitarbeiter'],
         'Zeitdifferenz': []
      }
      if id == None:
         tempDataErr = self.db_o.ReadErrorData()
         for item in tempDataErr.values():
            retVal_o['Data'].append({'Beschreibung':item['Beschreibung'],'Projekt':item['Projekt'],'Komponente':item['Komponente'],'Status':item['Status']})

            if item['Status'] == "Behoben":
               t1 = datetime.datetime.strptime(item['Datum'], "%Y-%m-%d")
               t2 = datetime.datetime.strptime(item['DatumDerBeseitigung'], "%Y-%m-%d")
               tdiff = t2 - t1
               retVal_o['Zeitdifferenz'].append(str(tdiff))
            else:
               retVal_o['Zeitdifferenz'].append("Noch nicht fertiggestellt")

         retVal_o['Data'].sort(key=lambda x: x['Projekt'])
         retVal_o['Rolle'] = globals()['AngemeldeterMitarbeiter']

      List = []
      List.append(retVal_o)
      retVal_s = self.app.getList_p(List)
      print(retVal_s)
      return retVal_s


class Login_cl(object):
   exposed = True

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()
      self.template_o = Template_cl()
      self.app = Application_cl()


   #-------------------------------------------------------
   def GET(self, status=None):
   #-------------------------------------------------------
      retVal_s = ''
      if status == 'logout':
         globals()['AngemeldeterMitarbeiter'] = None

      List = []
      List.append({})
      retVal_s = self.app.getList_p(List)
      return retVal_s

   #-------------------------------------------------------
   def POST(self, **data_opl):
   #-------------------------------------------------------
      retVal_s = ''
      tmpVal = self.db_o.ReadLoginData(data_opl["Name"])
      if tmpVal == None:
         return "Fehler"
      else:
         globals()['AngemeldeterMitarbeiter'] = tmpVal['Rolle']
         print(AngemeldeterMitarbeiter)
         return "Erfolgreich"




# EOF
