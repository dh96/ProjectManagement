# coding: utf-8

import json
import datetime

import os
import os.path
import codecs

class Database_cl(object):
    def __init__(self):
        self.project_data = {}
        self.employeeQS_data = {}
        self.employeeSW_data = {}
        self.component_data = {}
        self.error_data = {}
        self.categoryError_data = {}
        self.categoryCause_data = {}
        self.login_data = {}
        pass


    def readData(self, file_name):
        path_s = "/Users/DennisHalter/Desktop/WEB3_Prak/webNext_Final3/bt/data/" + file_name
        with codecs.open(path_s, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def saveData(self, file_name, data):
        path_s = "/Users/DennisHalter/Desktop/WEB3_Prak/webNext_Final3/bt/data/" + file_name
        with codecs.open(path_s, 'w', encoding='utf-8') as output:
            json.dump(data, output, indent=3)

    def GetMaxID(self, file_name):
        return self.readData(file_name)

    def UpdateMaxID(self, file_name):
        self.saveData(file_name, self.readData(file_name)+1)

# ----------------------------------------------------------
#ProjectData
# ----------------------------------------------------------
    def ReadProjectData(self):
        try:
            self.project_data = self.readData('Project/Project.json')
        except:
            self.project_data = {}
        return self.project_data

    def AddProject(self, data):
        self.project_data[self.GetMaxID('Project/maxId.json')] = data
        self.UpdateMaxID('Project/maxId.json')
        self.saveData('Project/Project.json', self.project_data)

    def GetProjectMaxId(self):
        return self.GetMaxID('Project/maxId.json')

    def UpdateProject(self, id_s, data):
        self.project_data[id_s] = data
        self.saveData('Project/Project.json', self.project_data)

    def DeleteProject(self, id_s):
        if self.project_data.pop(id_s, None) != None:
            self.saveData('Project/Project.json', self.project_data)
        else:
            return "There is no Project with this Id"

    def GetProjectData(self, id_s):
        self.ReadProjectData()
        try:
            project = self.project_data[id_s]
        except:
            project= self.GetDefaultProjectData()
        return project

    def GetDefaultProjectData(self):
        return { "id":'-1', "Name": '' } # EOF

# ----------------------------------------------------------
#KomponenteData
# ----------------------------------------------------------
    def ReadComponentData(self):
        try:
            self.component_data = self.readData('Components/components.json')
        except:
            self.component_data = {}
        return self.component_data

    def AddComponent(self, data):
        self.component_data[self.GetMaxID('Components/maxId.json')] = data
        self.UpdateMaxID('Components/maxId.json')
        self.saveData('Components/components.json', self.component_data)

    def GetComponentMaxId(self):
        return self.GetMaxID('Components/maxId.json')

    def UpdateComponent(self, id_s, data):
        self.component_data[id_s] = data
        self.saveData('Components/components.json', self.component_data)

    def DeleteComponent(self, id_s):
        if self.component_data.pop(id_s, None) != None:
            self.saveData('Components/components.json', self.component_data)
        else:
            return "There is no Component with this Id"

    def GetComponentData(self, id_s):
        self.ReadComponentData()
        try:
            komponente = self.component_data[id_s]
        except:
            komponente= self.GetDefaultComponentData()
        return komponente

    def GetDefaultComponentData(self):
        return  { "id":'-1', 'Projekt':None, 'Komponente' : '' }


# ----------------------------------------------------------
#MitarbeiterSWData
# ----------------------------------------------------------
    def ReadEmployeeSWData(self):
        try:
            self.employeeSW_data = self.readData('EmployeeSW/Employee.json')
        except:
            self.employeeSW_data = {}
        return self.employeeSW_data

    def AddEmployeeSW(self, data):
        self.employeeSW_data[self.GetMaxID('EmployeeSW/maxId.json')] = data
        self.UpdateMaxID('EmployeeSW/maxId.json')
        self.saveData('EmployeeSW/Employee.json', self.employeeSW_data)

    def GetEmployeeSWMaxId(self):
        return self.GetMaxID('EmployeeSW/maxId.json')

    def UpdateEmployeeSW (self, id_s, data):
        self.employeeSW_data[id_s] = data
        self.saveData('EmployeeSW/Employee.json', self.employeeSW_data)

    def DeleteEmployeeSW(self, id_s):
        if self.employeeSW_data.pop(id_s, None) != None:
            self.saveData('EmployeeSW/Employee.json', self.employeeSW_data)
        else:
            return "There is no EmployeeSW with this Id"

    def GetEmployeeSWData(self, id_s):
        self.ReadEmployeeSWData()
        try:
            mitarbeiterSW = self.employeeSW_data[id_s]
        except:
            mitarbeiterSW= self.GetDefaultEmployeeSWData()
        return mitarbeiterSW

    def GetDefaultEmployeeSWData(self):
        return  { "id":'-1', 'Name':None, 'Vorname' : '' , 'Abteilung':'SW'}

# EOF

# ----------------------------------------------------------
#MitarbeiterQSData
# ----------------------------------------------------------
    def ReadEmployeeQSData(self):
        try:
            self.employeeQS_data = self.readData('EmployeeQS/Employee.json')
        except:
            self.employeeQS_data = {}
        return self.employeeQS_data

    def AddEmployeeQS(self, data):
        self.employeeQS_data[self.GetMaxID('EmployeeQS/maxId.json')] = data
        self.UpdateMaxID('EmployeeQS/maxId.json')
        self.saveData('EmployeeQS/Employee.json', self.employeeQS_data)

    def GetEmployeeQSMaxId(self):
        return self.GetMaxID('EmployeeQS/maxId.json')

    def UpdateEmployeeQS (self, id_s, data):
        self.employeeQS_data[id_s] = data
        self.saveData('EmployeeQS/Employee.json', self.employeeQS_data)

    def DeleteEmployeeQS(self, id_s):
        if self.employeeQS_data.pop(id_s, None) != None:
            self.saveData('EmployeeQS/Employee.json', self.employeeQS_data)
        else:
            return "There is no EmployeeQS with this Id"

    def GetEmployeeQSData(self, id_s):
        self.ReadEmployeeQSData()
        try:
            mitarbeiterQS = self.employeeQS_data[id_s]
        except:
            mitarbeiterQS= self.GetDefaultEmployeeQSData()
        return mitarbeiterQS

    def GetDefaultEmployeeQSData(self):
        return  { "id":'-1', 'Name':None, 'Vorname' : '' , 'Abteilung':'QS'}



# ----------------------------------------------------------
#KategorieFehler
# ----------------------------------------------------------
    def ReadCatErrorData(self):
        try:
            self.categoryError_data = self.readData('CategorieError/CatError.json')
        except:
            self.categoryError_data = {}
        return self.categoryError_data

    def AddCatError(self, data):
        self.categoryError_data[self.GetMaxID('CategorieError/maxId.json')] = data
        self.UpdateMaxID('CategorieError/maxId.json')
        self.saveData('CategorieError/CatError.json', self.categoryError_data)

    def GetCatErrorMaxId(self):
        return self.GetMaxID('CategorieError/maxId.json')

    def UpdateCatError (self, id_s, data):
        self.categoryError_data[id_s] = data
        self.saveData('CategorieError/CatError.json', self.categoryError_data)

    def DeleteCatError(self, id_s):
        if self.categoryError_data.pop(id_s, None) != None:
            self.saveData('CategorieError/CatError.json', self.categoryError_data)
        else:
            return "There is no Kat with this Id"

    def GetCatErrorData(self, id_s):
        self.ReadCatErrorData()
        try:
            catErr = self.categoryError_data[id_s]
        except:
            catErr = self.GetDefaultCatErrorData()
        return catErr

    def GetDefaultCatErrorData(self):
        return  { "id":'-1', 'Beschreibung':None, 'src':'Fehler'}

# ----------------------------------------------------------
#KategorieCause
# ----------------------------------------------------------
    def ReadCatCauseData(self):
        try:
            self.categoryCause_data = self.readData('CategorieCause/CatCause.json')
        except:
            self.categoryCause_data = {}
        return self.categoryCause_data

    def AddCatCause(self, data):
        self.categoryCause_data[self.GetMaxID('CategorieCause/maxId.json')] = data
        self.UpdateMaxID('CategorieCause/maxId.json')
        self.saveData('CategorieCause/CatCause.json', self.categoryCause_data)

    def GetCatCauseMaxId(self):
        return self.GetMaxID('CategorieCause/maxId.json')

    def UpdateCatCause (self, id_s, data):
        self.categoryCause_data[id_s] = data
        self.saveData('CategorieCause/CatCause.json', self.categoryCause_data)

    def DeleteCatCause(self, id_s):
        if self.categoryCause_data.pop(id_s, None) != None:
            self.saveData('CategorieCause/CatCause.json', self.categoryCause_data)
        else:
            return "There is no Kat with this Id"

    def GetCatCauseData(self, id_s):
        self.ReadCatCauseData()
        try:
            catErr = self.categoryCause_data[id_s]
        except:
            catErr = self.GetDefaultCatCauseData()
        return catErr

    def GetDefaultCatCauseData(self):
        return  { "id":'-1', 'Beschreibung':None, 'src':'Ursache'}

# ----------------------------------------------------------
#Fehler
# ----------------------------------------------------------
    def ReadErrorData(self):
        try:
            self.error_data = self.readData('Error/Error.json')
        except:
            self.error_data = {}
        return self.error_data

    def AddError(self, data):
        self.error_data[self.GetMaxID('Error/maxId.json')] = data
        self.UpdateMaxID('Error/maxId.json')
        self.saveData('Error/Error.json', self.error_data)

    def GetErrorMaxId(self):
        return self.GetMaxID('Error/maxId.json')

    def UpdateError (self, id_s, data):
        self.error_data[id_s] = data
        self.saveData('Error/Error.json', self.error_data)

    def DeleteError(self, id_s):
        if self.error_data.pop(id_s, None) != None:
            self.saveData('Error/Error.json', self.error_data)
        else:
            return "There is no Error with this Id"

    def GetErrorData(self, id_s):
        self.ReadErrorData()
        try:
            err = self.error_data[id_s]
        except:
            err = self.GetDefaultErrorData()
        return err

    def GetDefaultErrorData(self):
        defaultObject = { "id":'-1', 'Beschreibung':'',
        'Datum':str(datetime.datetime.now().date())}
        return  defaultObject

# ----------------------------------------------------------
#Fehler
# ----------------------------------------------------------
    def ReadLoginData(self, username):

        try:

            self.login_data = self.readData("Login/" + username +".json")
        except:
            self.login_data = None

        return self.login_data
# EOF
