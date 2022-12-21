//------------------------------------------------------------------------------
//Demonstrator evs/tco/tmg
//------------------------------------------------------------------------------


'use strict'
var istAngemeldet = 0;
var zustand = "";
//------------------------------------------------------------------------------
class DetailView_cl {
//------------------------------------------------------------------------------

   constructor (el_spl, template_spl, path_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.path_s = path_spl;
   }
   render_px (id_spl) {
      let path_p = this.path_s + id_spl;
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.request_px(path_p,
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("Detail - render failed");
         }
      );
   }
   doRender_p (data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
         this.configHandleEvent_p();
      }
   }
   configHandleEvent_p () {
      let el_o = document.querySelector("form");
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      if (event_opl.target.id.includes("IdBack")) {
         APPUTIL.es_o.publish_px("app.cmd", [event_opl.target.id, null]);
         event_opl.preventDefault();
      }
      else if(event_opl.target.id.includes("Save")){;
         APPUTIL.es_o.publish_px("app.cmd", [event_opl.target.id, null]);
         event_opl.preventDefault();
      }
   }

}

//------------------------------------------------------------------------------
class ListView_cl {
//------------------------------------------------------------------------------

   constructor (el_spl, template_spl, path_spl, name_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.path_s = path_spl;
      this.name_s = name_spl;
      this.configHandleEvent_p();
   }
   render_px (id_spl=null, typen=null) {
      let path_p = this.path_s;
      if (id_spl != null)
      {
         path_p = path_p + id_spl;
      }
      if(typen != null)
      {
         path_p = path_p + typen;
      }
      let requester_o = new APPUTIL.Requester_cl();
      requester_o.request_px(path_p,
         function (responseText_spl) {
            let data_o = JSON.parse(responseText_spl);
            this.doRender_p(data_o);
         }.bind(this),
         function (responseText_spl) {
            alert("List - render failed");
         }
      );
   }
   doRender_p (data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      let z = event_opl.target.id.split(".");
      let teil = z[0];


      if (event_opl.target.tagName.toUpperCase() == "TD") {
         let elx_o = document.querySelector(".clSelected");
         if (elx_o != null) {
            elx_o.classList.remove("clSelected");
         }
         event_opl.target.parentNode.classList.add("clSelected");
         event_opl.preventDefault();
      } else if ((event_opl.target.id == "idShowListEntry") || (event_opl.target.id == teil + ".Edit")){
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            APPUTIL.es_o.publish_px("app.cmd", [teil + ".Edit", elx_o.id] );
         }
         event_opl.preventDefault();
      }else if(event_opl.target.id == teil + ".Delete"){
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            if(!confirm("Möchten Sie wirklich löschen?"))
            {
               event_opl.preventDefault();
            }else{
               APPUTIL.es_o.publish_px("app.cmd", [teil + ".Delete", elx_o.id] );
            }
         }
         event_opl.preventDefault();
      }
      else if(event_opl.target.id == teil + ".check"){
         let elx_o = document.querySelector(".clSelected");
         if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } else {
            if(!confirm("War die Prüfung erfolgreich"))
            {
               APPUTIL.es_o.publish_px("app.cmd", [teil + ".check", "fehlgeschlagen",elx_o.id] );
            }else{

               APPUTIL.es_o.publish_px("app.cmd", [teil + ".check", "erfolgreich",elx_o.id] );
            }
         }
         event_opl.preventDefault();
      }
      else if(event_opl.target.id == teil + ".Add"){
         APPUTIL.es_o.publish_px("app.cmd", [teil + ".Add", null] );
      }
      else if(event_opl.target.id == "MitarbeiterSW"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == "MitarbeiterQS"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == "KategorieFehler"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == "KategorieUrsache"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == "erkannteFehler"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , "type=erkannt"] );
      }
      else if(event_opl.target.id == "behobeneFehler"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , "type=behoben"] );
      }
      else if(event_opl.target.id == "AuswertungKategorie"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == "AuswertungProjekt"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == "AuswertungProjektZeit"){
         APPUTIL.es_o.publish_px("app.cmd", [teil , null] );
      }
      else if(event_opl.target.id == teil +".Auswahl"){
         var selector = document.getElementById('Projekt');
         var value = selector[selector.selectedIndex].id;
         APPUTIL.es_o.publish_px("app.cmd", [teil +".Auswahl" , value] );
      }
      else if(event_opl.target.id == teil + ".Anmelden"){
         APPUTIL.es_o.publish_px("app.cmd", [teil + ".Anmelden" , null] );
      }

   }
}



//------------------------------------------------------------------------------
class SideBar_cl {
//------------------------------------------------------------------------------

   constructor (el_spl, template_spl) {
      this.el_s = el_spl;
      this.template_s = template_spl;
      this.configHandleEvent_p();
   }
   render_px (data_opl) {
      let markup_s = APPUTIL.tm_o.execute_px(this.template_s, data_opl);
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.innerHTML = markup_s;
      }
   }
   configHandleEvent_p () {
      let el_o = document.querySelector(this.el_s);
      if (el_o != null) {
         el_o.addEventListener("click", this.handleEvent_p);
      }
   }
   handleEvent_p (event_opl) {
      let cmd_s = event_opl.target.dataset.action;
      APPUTIL.es_o.publish_px("app.cmd", [cmd_s, null]);
   }
}

class Application_cl {

   constructor () {
      // Registrieren zum Empfang von Nachrichten
      APPUTIL.es_o.subscribe_px(this, "templates.loaded");
      APPUTIL.es_o.subscribe_px(this, "templates.failed");
      APPUTIL.es_o.subscribe_px(this, "app.cmd");
      this.sideBar_o = new SideBar_cl("aside", "sidebar.tpl.html");
      this.login_o = new ListView_cl("main", "Anmeldung.tpl.html", "/login/", "Login");
      this.listProject_o = new ListView_cl("main", "Projekt.tpl.html", "/projekt/", "Projekte");
      this.detailProject_o = new DetailView_cl("main","ProjektForm.tpl.html", "/projekt/");
      this.listKomponente_o = new ListView_cl("main", "Komponenten.tpl.html", "/komponente/", "Komponente");
      this.listProjektKomponenten_o = new ListView_cl("main", "Komponenten.tpl.html", "/projektkomponenten/", "Komponente");
      this.detailKomponente_o = new DetailView_cl("main","KomponenteForm.tpl.html", "/komponente/");
      this.listMitarbeiter_o = new ListView_cl("main", "Mitarbeiter.tpl.html", "/mitarbeiter/", "Mitarbeiter");
      this.listMitarbeiterSW_o = new ListView_cl("main", "MitarbeiterSW.tpl.html", "/swentwickler/", "MitarbeiterSW");
      this.detailMitarbeiterSW_o = new DetailView_cl("main","MitarbeiterSWForm.tpl.html", "/swentwickler/");
      this.listMitarbeiterQS_o = new ListView_cl("main", "MitarbeiterQS.tpl.html", "/qsmitarbeiter/", "MitarbeiterQS");
      this.detailMitarbeiterQS_o = new DetailView_cl("main","MitarbeiterQSForm.tpl.html", "/qsmitarbeiter/");
      this.listKategorien_o = new ListView_cl("main", "Kategorien.tpl.html", "/kat/", "Kategorien");
      this.listKategorieFehler_o = new ListView_cl("main", "KatFehler.tpl.html", "/katfehler/", "KategorieFehler");
      this.detailKategorieFehler_o = new DetailView_cl("main","KatFehlerForm.tpl.html", "/katfehler/");
      this.listKategorieUrsache_o = new ListView_cl("main", "KatUrsache.tpl.html", "/katursache/", "KategorieUrsache");
      this.detailKategorieUrsache_o = new DetailView_cl("main","KatUrsacheForm.tpl.html", "/katursache/");
      this.listFehler_o = new ListView_cl("main", "Fehler.tpl.html", "/fehler/", "Fehler");
      this.listFehlerErkannt_o = new ListView_cl("main", "ErkannteFehler.tpl.html", "/fehler/", "FehlerErkannt");
      this.detailFehlerErkannt_o = new DetailView_cl("main","ErkannteFehlerForm.tpl.html", "/fehler/");
      this.detailFehlerErkannt1_o = new DetailView_cl("main","ErkannteFehlerBearbeitenForm.tpl.html", "/fehler/");
      this.listFehlerBehoben_o = new ListView_cl("main", "BehobenFehler.tpl.html", "/fehler/", "FehlerBehoben");
      this.listAuswertungKategorie_o = new ListView_cl("main", "AuswertungKategorie.tpl.html", "/katlist/", "AuswertungKategorie");
      this.listAuswertungProjekte_o = new ListView_cl("main", "AuswertungProjekte.tpl.html", "/prolist/", "AuswertungProjekte");
      this.listAuswertungProjekteZeit_o = new ListView_cl("main", "AuswertungProjekteZeit.tpl.html", "/prozeitlist/", "AuswertungProjekteZeit");
   }

   notify_px (self, message_spl, data_opl) {
      switch (message_spl) {
      case "templates.failed":
         alert("Vorlagen konnten nicht geladen werden.");
         break;
      case "templates.loaded":
         let markup_s;
         let el_o;
         markup_s = APPUTIL.tm_o.execute_px("headerBT.tpl.html", null);
         el_o = document.querySelector("header");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         let nav_a = [
            ["Login", "Anmelden"],
            ["Fehlerdaten", "Bearbeitung Fehlerdaten"],
            ["Projekte", "Pflege Projekte"],
            ["Komponenten", "Pflege Komponenten"],
            ["Mitarbeiter", "Pflege Mitarbeiter"],
            ["Kategorien", "Pflege Kategorien"],
            ["AuswertungProjekt", "Auswertung Projekt/Fehler"],
            ["AuswertungProjektZeit", "Auswertung Projekt/Fehler/Zeit"],
            ["AuswertungKategorie", "Auswertung Kategorie/Fehler"],
            ["Logout", "Abmelden"]
         ];
         self.sideBar_o.render_px(nav_a);
         markup_s = APPUTIL.tm_o.execute_px("home.tpl.html", null);
         el_o = document.querySelector("main");
         if (el_o != null) {
            el_o.innerHTML = markup_s;
         }
         break;

      case "app.cmd":
         // hier müsste man überprüfen, ob der Inhalt gewechselt werden darf
         switch (data_opl[0]) {
         case "home":
            let markup_s = APPUTIL.tm_o.execute_px("home.tpl.html", null);
            let el_o = document.querySelector("main");
            if (el_o != null) {
               el_o.innerHTML = markup_s;
            }
            let markup_sh = APPUTIL.tm_o.execute_px("headerBT.tpl.html", null);
            let el_sh = document.querySelector("header");
            if (el_sh != null) {
               el_sh.innerHTML = markup_sh;
            }
            break;
         case "Login":
            if(istAngemeldet == 1){
               alert("Bitte abmelden");
               break;
            }else {
               this.login_o.render_px();
               break;
            }
         case "Login.Anmelden":
            const request = async() => {
               const response = await fetch('/login', {
               method: 'POST',
               headers: {
                  'Content-Type': 'application/x-www-form-urlencoded'
               },
               body: "Name=" + document.getElementById('Benutzername').value
               + "&Passwort=" + document.getElementById('Passwort').value
            }).then((response_opl)  => {
               let retVal_o = null;
               retVal_o = response_opl.text().then((text_spl) => {
                  if(text_spl == "Erfolgreich"){
                     istAngemeldet = 1;
                     this.listProject_o.render_px();
                  }
                  else{
                     alert(text_spl);
                  }
               });
               return retVal_o;
            });
            }
            request();
            break;
         case "Logout":
            if(istAngemeldet == 1){
               this.login_o.render_px("logout");
               istAngemeldet = 0;
            break;
            }
            else {
               alert("Bitte anmelden!");
               break;
            }

         case "Projekte":
            if(istAngemeldet == 1){
               this.listProject_o.render_px();
               break;
            }else{
               alert("Bitte melden Sie sich zuerst an!");
               break;
            }

         case "Projekte.Add":
            this.detailProject_o.render_px();
            break;
         case "Projekte.Edit":
            this.detailProject_o.render_px(data_opl[1]);
            break;
         case "Projekte.IdBack":
            this.listProject_o.render_px();
            break;
        case "Projekte.Save":
            if(document.getElementById('id').value == "-1")
            {
               const request = async() => {
                  const response = await fetch('/projekt', {
                     method: 'POST',
                     headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                      },
                     body: "Name=" + document.getElementById('ProjectName').value
                  }).then(response => this.listProject_o.render_px());
               }
               request();
            }
            else {
               const request = async() => {
                  const response = await fetch('/projekt', {
                     method: 'PUT',
                     headers: {
                       'Content-Type': 'application/x-www-form-urlencoded'
                     },
                   body: "id=" + document.getElementById('id').value + "&Name=" + document.getElementById('ProjectName').value
                }).then(response => this.listProject_o.render_px());
               }
               request();
            }
            break;
        case "Projekte.Delete":
            const pdelete = async() => {
            const response = await fetch('/projekt/' +  data_opl[1] , {
               method: 'DELETE',
               headers: {
                  'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(response => this.listProject_o.render_px());
            }
            pdelete();
            break;
      case "Komponenten":
         if(istAngemeldet == 1){
            this.listKomponente_o.render_px();
         break;
         }else {
            alert("Bitte melden Sie sich zuerst an!");
            break;
         }

      case "Komponente.Auswahl":
         this.listProjektKomponenten_o.render_px(data_opl[1]);
         break;
      case "Komponente.Add":
         this.detailKomponente_o.render_px();
         break;
      case "Komponente.Edit":
         this.detailKomponente_o.render_px(data_opl[1]);
         break;
      case "Komponente.IdBack":
         this.listKomponente_o.render_px();
         break;
     case "Komponente.Save":
         if(document.getElementById('id').value == "-1")
         {
            const ksave = async() => {
             const response = await fetch('/komponente', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
                body: "Projekt=" + document.getElementById('Projekt').value + "&Komponente=" + document.getElementById('Komponente').value
             }).then(response => this.listKomponente_o.render_px());
         }
         ksave();
         }

         else {
            const ksave = async() => {
            const response = await fetch('/komponente', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + document.getElementById('id').value + "&Projekt=" + document.getElementById('Projekt').value + "&Komponente=" + document.getElementById('Komponente').value
            }).then(response => this.listKomponente_o.render_px());
         }
         ksave();
         }

         break;
     case "Komponente.Delete":
      const kdelete = async() => {
        const response = fetch('/komponente/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(response => this.listKomponente_o.render_px());
         }
         kdelete();
         break;
      case "Mitarbeiter":
         if(istAngemeldet == 1){
            this.listMitarbeiter_o.render_px();
            break;
         }else{
            alert("Bitte melden Sie sich zuerst an!");
            break;
         }
      case "MitarbeiterSW":
         var elem = document.getElementById("AngemeldeteMitarbeiterRolle").value;
         if(elem == "SW"){
            this.listMitarbeiterSW_o.render_px();
            break;
         }else {
            alert("nicht angemeldet");
            break;
         }
      case "MitarbeiterSW.Add":
         this.detailMitarbeiterSW_o.render_px();
         break;
      case "MitarbeiterSW.Edit":
         this.detailMitarbeiterSW_o.render_px(data_opl[1]);
         break;
      case "MitarbeiterSW.IdBack":
         this.listMitarbeiterSW_o.render_px();
         break;
     case "MitarbeiterSW.Save":
         if(document.getElementById('id').value == "-1")
         {
            const request = async() => {
             const response = await fetch('/swentwickler', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
                body: "Name=" + document.getElementById('Name').value
                + "&Vorname=" + document.getElementById('Vorname').value
                + "&Abteilung=" + document.getElementById('Abteilung').value
             }).then(response => this.listMitarbeiterSW_o.render_px());
            }
            request();
         }
         else {
            const request = async() => {
               const response = await fetch('/swentwickler', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + document.getElementById('id').value
               + "&Name=" + document.getElementById('Name').value
               + "&Vorname=" + document.getElementById('Vorname').value
               + "&Abteilung=" + document.getElementById('Abteilung').value
            }).then(response => this.listMitarbeiterSW_o.render_px());
         }
         request();
         }
         break;
     case "MitarbeiterSW.Delete":
     const mswdelete = async() => {
         const response = await fetch('/swentwickler/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(response => this.listMitarbeiterSW_o.render_px());
         }
         mswdelete();
         break;
      case "MitarbeiterQS":
         var elem = document.getElementById("AngemeldeteMitarbeiterRolle").value;
         if(elem == "QS"){
            this.listMitarbeiterQS_o.render_px();
            break;
         }else {
            alert("Zugriff verweigert!");
            break;
         }

      case "MitarbeiterQS.Add":
         this.detailMitarbeiterQS_o.render_px();
         break;
      case "MitarbeiterQS.Edit":
         this.detailMitarbeiterQS_o.render_px(data_opl[1]);
         break;
      case "MitarbeiterQS.IdBack":
         this.listMitarbeiterQS_o.render_px();
         break;
     case "MitarbeiterQS.Save":
         if(document.getElementById('id').value == "-1")
         {
            const request = async() => {
             const response = await fetch('/qsmitarbeiter', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
                body: "Name=" + document.getElementById('Name').value
                + "&Vorname=" + document.getElementById('Vorname').value
                + "&Abteilung=" + document.getElementById('Abteilung').value
             }).then(response => this.listMitarbeiterQS_o.render_px());
            }
            request();
         }
         else {
            const request = async() => {
               const response = await fetch('/qsmitarbeiter', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + document.getElementById('id').value
               + "&Name=" + document.getElementById('Name').value
               + "&Vorname=" + document.getElementById('Vorname').value
               + "&Abteilung=" + document.getElementById('Abteilung').value
            }).then(response => this.listMitarbeiterQS_o.render_px());
         }
         request();
         }
         break;
     case "MitarbeiterQS.Delete":
     const mqsdelete = async() => {
      const response = await fetch('/qsmitarbeiter/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(response => this.listMitarbeiterQS_o.render_px());
         }
         mqsdelete();
         break;
      case "Kategorien":
         if(istAngemeldet == 1){
            this.listKategorien_o.render_px();
            break;
         }else{
            alert("Bitte melden Sie sich zuerst an!");
            break;
         }

      case "KategorieFehler":
         this.listKategorieFehler_o.render_px();
         break;
      case "KategorieFehler.Add":
         this.detailKategorieFehler_o.render_px();
         break;
      case "KategorieFehler.Edit":
         this.detailKategorieFehler_o.render_px(data_opl[1]);
         break;
      case "KategorieFehler.IdBack":
         this.listKategorieFehler_o.render_px();
         break;
      case "KategorieFehler.Save":
         if(document.getElementById('id').value == "-1")
         {
            const request = async() => {
             const response = await fetch('/katfehler/', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
                body: "id=" + document.getElementById('id').value
                + "&Beschreibung=" + document.getElementById('Beschreibung').value
                + "&src=" + document.getElementById('src').value
             }).then(response => this.listKategorieFehler_o.render_px());
            }
            request();
         }
         else {
            const request = async() => {
               const response = await fetch('/katfehler/', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + document.getElementById('id').value
               + "&Beschreibung=" + document.getElementById('Beschreibung').value
               + "&src=" + document.getElementById('src').value
            }).then(response => this.listKategorieFehler_o.render_px());
         }
         request();
         }
         break;
     case "KategorieFehler.Delete":
     const katdelete = async() => {
      const response = await fetch('/katfehler/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(response => this.listKategorieFehler_o.render_px());
         }
         katdelete();
         break;
         case "KategorieUrsache":
         this.listKategorieUrsache_o.render_px();
         break;
      case "KategorieUrsache.Add":
         this.detailKategorieUrsache_o.render_px();
         break;
      case "KategorieUrsache.Edit":
         this.detailKategorieUrsache_o.render_px(data_opl[1]);
         break;
      case "KategorieUrsache.IdBack":
         this.listKategorieUrsache_o.render_px();
         break;
      case "KategorieUrsache.Save":
         if(document.getElementById('id').value == "-1")
         {
            const request = async() => {
               const response = await fetch('/katursache/', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
                body: "id=" + document.getElementById('id').value
                + "&Beschreibung=" + document.getElementById('Beschreibung').value
                + "&src=" + document.getElementById('src').value
             }).then(response => this.listKategorieUrsache_o.render_px());
            }
            request();
         }
         else {
            const request = async() => {
               const response = await fetch('/katursache/', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + document.getElementById('id').value
               + "&Beschreibung=" + document.getElementById('Beschreibung').value
               + "&src=" + document.getElementById('src').value
            }).then(response => this.listKategorieUrsache_o.render_px());
            }
            request();
         }
         break;
     case "KategorieUrsache.Delete":
     const katudelete = async() => {
      const response = await fetch('/katursache/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(response => this.listKategorieUrsache_o.render_px());
         }
         katudelete();
         break;
      case "Fehlerdaten":
         if(istAngemeldet == 1){
            this.listFehler_o.render_px();
            break;
         }else {
            alert("Bitte melden sie sich zuerst an");
            break;
         }

      case "erkannteFehler":
      var elem = document.getElementById("AngemeldeteMitarbeiterRolle").value;
         if(elem == "QS" ||elem == "SW" ){
            this.listFehlerErkannt_o.render_px(null ,data_opl[1]);
            break;
         }else{
            alert("Falsch angemeldet");
            break;
         }
      case "behobeneFehler":
         this.listFehlerBehoben_o.render_px(null ,data_opl[1]);
         break;
      case "FehlerErkannt.IdBack":
         this.listFehlerErkannt_o.render_px();
         break;
      case "FehlerErkannt.Add":
         var elem = document.getElementById("AngemeldeteMitarbeiterRolle").value;
         if(elem == "QS"){
            this.detailFehlerErkannt_o.render_px();
            break;
         }else {
            alert("Falsch angemeldet");
            break;
         }
      case "FehlerErkannt.Edit":
         var elem = document.getElementById("AngemeldeteMitarbeiterRolle").value;
         if(elem == "SW"){
         this.detailFehlerErkannt1_o.render_px(data_opl[1]);
         }else {
            alert("Falsch angemeldet");
            break;
         }
         break;
      case "FehlerErkannt.Save":
         if(document.getElementById('id').value == "-1" || zustand == "fehlgeschlagen")
         {
            alert("Hier");
            const request = async() => {
               const response = await fetch('/fehler/', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
                body: "id=" + document.getElementById('id').value
                + "&Beschreibung=" + document.getElementById('Beschreibung').value
                + "&Mitarbeiter=" + document.getElementById('Mitarbeiter').value
                + "&Datum=" + document.getElementById('Datum').value
                + "&Komponente=" + document.getElementById('Komponente').value
                + "&Projekt=" + document.getElementById('Projekt').value
                + "&Status=" + document.getElementById('Status').value
                + "&FehlerKategorie=" + document.getElementById('FehlerKategorie').value
                + "&Zustand=" + "erfasst"
             }).then(response => this.listFehlerErkannt_o.render_px(null, "type=erkannt"));
            }
            request();
            zustand = "";
         }
         else {
            const request = async() => {
               const response = await fetch('/fehler/', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + document.getElementById('id').value
               + "&BeschreibungFehlerUrsache=" + document.getElementById('BeschreibungFehlerUrsache').value
               + "&MitarbeiterDerFehlerBehobenHat=" + document.getElementById('MitarbeiterDerFehlerBehobenHat').value
               + "&DatumDerBeseitigung=" + document.getElementById('DatumDerBeseitigung').value
               + "&KategorieFehlerUrsache=" + document.getElementById('KategorieFehlerUrsache').value
               + "&Status=" + "Behoben"
               + "&Zustand=" + zustand
            }).then(response => this.listFehlerErkannt_o.render_px(null, "type=erkannt"));
         }
         request();
         zustand = "";
         }
         break;
     case "FehlerErkannt.Delete":
     const ferkdelete = async() => {
      const response = await fetch('/fehler/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(this.listFehlerErkannt_o.render_px(null, "type=erkannt"));
         }
         ferkdelete();
         break;
      case "FehlerBehoben.Delete":
      const fbehdelete = async() => {
         const response = await fetch('/fehler/' +  data_opl[1] , {
            method: 'DELETE',
            headers: {
               'Content-Type': 'application/x-www-form-urlencoded'
             }
         }).then(response => this.listFehlerBehoben_o.render_px());
         }
         fbehdelete();
         break;
      case "FehlerBehoben.check":
         var elem = document.getElementById("AngemeldeteMitarbeiterRolle").value;
         if(elem == "QS"){
            if(data_opl[1] == "fehlgeschlagen"){
            alert(data_opl[1]);
            const request = async() => {
               const response = await fetch('/fehler/', {
                 method: 'PUT',
                 headers: {
                   'Content-Type': 'application/x-www-form-urlencoded'
                 },
               body: "id=" + data_opl[2]
               + "&Beschreibung=" + ""
               + "&Mitarbeiter=" + ""
               + "&Datum=" + ""
               + "&Komponente=" + ""
               + "&Projekt=" + ""
               + "&FehlerKategorie=" + ""
               + "&BeschreibungFehlerUrsache=" + ""
               + "&MitarbeiterDerFehlerBehobenHat=" + ""
               + "&DatumDerBeseitigung=" + ""
               + "&KategorieFehlerUrsache=" + ""
               + "&Status=" + "Erkannt"
               + "&Zustand=" + "fehlgeschlagen"
            }).then(response => this.detailFehlerErkannt_o.render_px(null));
         }
         zustand = "fehlgeschlagen";
         request();
      }
      else {
         alert(data_opl[2]);
         alert("Prüfung war erfolgreich");
         const request = async() => {
            const response = await fetch('/fehler/', {
              method: 'PUT',
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
              },
            body: "id=" + data_opl[2]
            + "&Status=" + "Behoben"
            + "&Zustand=" + "erfolgreich"
         }).then(response => this.listFehlerBehoben_o.render_px(null, "type=behoben"));
      }
      request();
      break;
      }
      }else {
            alert("Falsch angemeldet");
            break;
         }
         break;
      case "AuswertungKategorie":
      if(istAngemeldet == 1){
         this.listAuswertungKategorie_o.render_px();
         break;
      }else{
         alert("Bitte melden sie sich zuerst an");
         break;
      }
      case "AuswertungProjektZeit":
      if(istAngemeldet == 1){
         this.listAuswertungProjekteZeit_o.render_px();
         break;
      }else{
         alert("Bitte melden sie sich zuerst an");
         break;
      }
      case "AuswertungProjekt":
         if(istAngemeldet == 1){
            this.listAuswertungProjekte_o.render_px();
            break;
         }else{
            alert("Bitte melden sie sich zuerst an");
            break;
         }
      }
      break;
      }
   }
}

window.onload = function () {
   APPUTIL.es_o = new APPUTIL.EventService_cl();
   var app_o = new Application_cl();
   APPUTIL.createTemplateManager_px();
}
