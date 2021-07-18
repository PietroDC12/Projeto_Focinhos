<template>
  <nav
    class="navbar navbar-expand-md navbar-dark"
    style="background-color: #9bb694"
  >
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
 
      <ul class="navbar-nav mr-auto mt-2 ml-4 mt-lg-0">
        <li class="nav-item">
          <a class="nav-link" style="color: rgba(71, 82, 94, 100)" href="/"
            >Home</a
          >
        </li>

        <li class="nav-item">
          <a
            class="nav-link"
            style="color: rgba(71, 82, 94, 100)"
            href="/"
            >Adicionar Ficha</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            style="color: rgba(71, 82, 94, 100)"
            href="/"
            >Busca por Imagem</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            style="color: rgba(71, 82, 94, 100)"
            href="/"
            >Busca por ID</a
          >
        </li>
      </ul>
    </div>
  </nav>
</template>
 
<script>
export default {
  name: "NavBar",
};
</script>

<style>
.navbar-nav > li {
  padding-left: 7px;
  padding-right: 7px;
}
</style>