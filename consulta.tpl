
%include('header.tpl')
<table style="text-align:center;">
  <tr>
    <th>DNI</th>
    <th>Nombre</th>
    <th>Caballo</th>
    <th>Apuesta</th>
  </tr>
%for d in datos:
  <tr>
    <td>{{d[0]}}</td>
    <td>{{d[1]}}</td>
    <td>{{d[2]}}</td>
    <td>{{d[3]}}</td>
  </tr>
%end
</table>
%include('footer.tpl')
