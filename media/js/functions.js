/*
 *  Copyright (c) 2007 Jader Rubini
 *
 *  This file is part of Django Brasil Project Site.
 *
 *  Django Brasil Project is free software; you can redistribute it
 *  and/or modify it under the terms of the GNU General Public License
 *  as published by the Free Software Foundation; either version 3 of
 *  the License, or (at your option) any later version.
 *
 *  Django Brasil Project is distributed in the hope that it will be
 *  useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 *  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program. If not, see <http://www.gnu.org/licenses/>.
 *
 */


// Esta função "chama" todas as funções usadas em um documento.
function init() {
	odd('ul');
	odd('ol');
	altRowColor();
	getLast('ul');
	getLast('ol');
	createExternalLinks();
}
addEvent(window, "load", init);
// --------------------



// Adiciona a função (fn) ao evento (evType) do objeto (obj)
function addEvent(obj, evType, fn){
   if (obj.addEventListener){
	  obj.addEventListener(evType, fn, true)}
   if (obj.attachEvent){
	  obj.attachEvent("on"+evType, fn)}
}
// --------------------



// Extensão do getElementById(id), permitindo o uso de classes
// Autor: Náiron - www.elmicox.com
function DOMgetElementsByClassName($node,$className){
    var $node, $atual, $className, $retorno = new Array(), $novos = new Array();
    $retorno = new Array();
    for (var $i=0;$i<$node.childNodes.length;$i++){
       $atual = $node.childNodes[$i];
       if($atual.nodeType==1){// 1 = XML_ELEMENT_NODE
          $classeAtual = $atual.className;
          if(new RegExp("\\b"+$className+"\\b").test($classeAtual)){
             $retorno[$retorno.length] = $atual;
          }
          if($atual.childNodes.length>0){
             $novos = DOMgetElementsByClassName($atual,$className);
             if($novos.length>0){
                $retorno = $retorno.concat($novos);
             }
          }
       }
    }
    return $retorno;
}
// --------------------



// Função pra alternar a cor dos itens de listas, adicionando a classe 'odd' aos itens pares
function odd(list_type) {
	var list = document.getElementsByTagName(list_type);

	for(i=0; i<list.length; i++){
		var li = list[i].getElementsByTagName('li');

		for (var j=0; j<li.length; j++){
			if (j % 2 == 0) { li[j].className += ' odd'; }
		}
	}
}

// --------------------



// Adiciona a classe "ultimo" ao ultimo elemento das listas
function getLast(list_type) {
	var list = document.getElementsByTagName(list_type);

	for(i=0; i<list.length; i++){
		var li = list[i].getElementsByTagName('li');
		var j = li.length - 1;
		li[j].className += ' ultimo';
	}
}
// --------------------



// Alternar as cores de TRs
// Author: Cadu de Castro Alves - http://www.cadudecastroalves.com 
function altRowColor() {
  var objTables = document.getElementsByTagName('tbody');
  var tableQty = objTables.length;

  for(i = 0; i < tableQty; i++) {
    var rowQty = objTables[i].rows.length;
    for(j = 0; j < rowQty; j++) {
      if(j % 2 == 0) {
        objTables[i].rows[j].className += ' odd';
      }
    }
  }
}
// --------------------



// Procura por links com rel="external" e faz com que eles abram em uma nova janela
// Autor: Henrique C. Pereira - http://www.revolucao.etc.br
function createExternalLinks() {
    if(document.getElementsByTagName) {
        var anchors = document.getElementsByTagName('a');
        for(var i=0; i<anchors.length; i++) {
            var anchor = anchors[i];
            if(anchor.getAttribute("href") && anchor.getAttribute('rel')=='external') {
                anchor.target = '_blank';
                var title = anchor.title + ' (Este link abre uma nova janela)';
                anchor.title = title;
            }
        }
    }
}
// --------------------