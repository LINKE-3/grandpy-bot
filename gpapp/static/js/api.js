const userinput = document.getElementById('userinput');

const button = document.getElementById('valu');
//addEventListener(<event>, <callback>)
button.addEventListener('click', function() {          // On écoute l'événement click
   console.log(userinput.value);               // On change le contenu de notre élément pour afficher "C'est cliqué !"
   historique.innerHTML += userinput.value+" ,";
   let form = new FormData()
   form.append("value",userinput.value)
   fetch("http://127.0.0.1:5000/url",{method:"post",body:form})
      .then(reponse => reponse.json())
      .then(reponse2 => { console.log(reponse2)
      output.innerHTML = reponse2.wikipedia;
      outurl.href = reponse2.wikipedia2;
      outurl.innerHTML = "plus d'information";
      outmap.src = reponse2.map;
   })
      //if wiki n'a pas de valeur
      //historique de recherche
});