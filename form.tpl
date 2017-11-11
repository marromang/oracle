
% include('header.tpl')

<div class="wrapper row3">
<main class="container clear"> 
	<article>
		<form action="apuestas" method="post"> 
			Codigo de la carrera de la que quieres saber las apuestas: <input name="carrera" type="text">
				<input value="Obtener informacion de las apuestas" type="submit">
		</form>
	</article>
</main>	
</div>

%include('footer.tpl')
