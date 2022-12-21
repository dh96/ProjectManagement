# coding:utf-8

# Demonstrator es/te/tm

import sys
import os.path
import cherrypy

from app import application, template

#----------------------------------------------------------
def main():
#----------------------------------------------------------

   # aktuelles Verzeichnis ermitteln, damit es in der Konfigurationsdatei als
   # Bezugspunkt verwendet werden kann
   try:                                    # aktuelles Verzeichnis als absoluter Pfad
      currentDir_s = os.path.dirname(os.path.abspath(__file__))
   except:
      currentDir_s = os.path.dirname(os.path.abspath(sys.executable))
   cherrypy.Application.currentDir_s = currentDir_s

   configFileName_s = os.path.join(currentDir_s, 'server.conf') # im aktuellen Verzeichnis
   if os.path.exists(configFileName_s) == False:
      # Datei gibt es nicht
      configFileName_s = None

   # autoreload-Monitor hier abschalten
   cherrypy.engine.autoreload.unsubscribe()

   # 1. Eintrag: Standardverhalten, Berücksichtigung der Konfigurationsangaben im configFile
   cherrypy.tree.mount(
      None, '/', configFileName_s
   )

   # 2. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
      application.Application_cl(),
      '/app',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

    #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
      application.Projekt_cl(),
      '/projekt',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
        application.Komponente_cl(), 
        '/komponente',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.tree.mount(
        application.ProjektKomponenten_cl(), 
        '/projektkomponenten',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
        application.Mitarbeiter_cl(), 
        '/mitarbeiter',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
        application.MitarbeiterSW_cl(), 
        '/swentwickler',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
        application.MitarbeiterQS_cl(), 
        '/qsmitarbeiter',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

    #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
        application.Kategorie_cl(), 
        '/kat',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )  

   #3. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
   cherrypy.tree.mount(
        application.KategorieFehler_cl(), 
        '/katfehler',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.tree.mount(
        application.KategorieUrsache_cl(), 
        '/katursache',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )
   cherrypy.tree.mount(
        application.FehlerErkannt_cl(), 
        '/fehler',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )
   cherrypy.tree.mount(
        application.AuswertungKat_cl(), 
        '/katlist',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )
   cherrypy.tree.mount(
        application.AuswertungPro_cl(), 
        '/prolist',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.tree.mount(
        application.AuswertungProZeit_cl(), 
        '/prozeitlist',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.tree.mount(
        application.Login_cl(), 
        '/login',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   # 2. Eintrag: Method-Dispatcher für die "Applikation" "templates" vereinbaren
   cherrypy.tree.mount(
      template.Template_cl(),
      '/templates',
      {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
   )

   cherrypy.engine.start()
   cherrypy.engine.block()

#----------------------------------------------------------
if __name__ == '__main__':
#----------------------------------------------------------
   main()
