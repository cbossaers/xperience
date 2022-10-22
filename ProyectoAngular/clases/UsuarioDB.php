<?php 

    function AddUsuario() {  }
    function UpdateUsuario() {  }
    function DeleteUsuario() {  }
    function GetUsuarioByCorreo() {  }
    function GetUsuarioById() {  }

    class Usuario { //no la borro por si acaso

        private int $id;
        private string $nombre;
        private string $apellidos;
        private string $contrasena;
        private string $correo;
        private $telefono;
        private DateTime $fechaNac;
        private string $dni;
        private string $dirPost;
        private string $dirFact;

        function __construct(int $id, string $nombre, string $apellidos, string $contrasena, string $correo) {
            $this -> id = $id;
            $this -> nombre = $nombre;
            $this -> apellidos = $apellidos;
            $this -> correo = $correo;
            $this -> contrasena = $contrasena;
        }

        public function getId() { return $this -> id; }
        public function setId(int $id) { $this -> id = $id; }

        public function getNombre() { return $this -> nombre; }
        public function setNombre(string $nombre) { $this -> nombre = $nombre; }

        public function getApellidos() { return $this -> apellidos; }
        public function setApellidos(string $apellidos) { $this -> apellidos = $apellidos; }

        public function getContrasena() { return $this -> contrasena; }
        public function setContrasena(string $contrasena) { $this -> contrasena = $contrasena; }

        public function getCorreo() { return $this -> correo; }
        public function setCorreo(string $correo) { $this -> correo = $correo; }

        public function getTelefono() { return $this -> telefono; }
        public function setTelefono($telefono) { $this -> telefono = $telefono; }

        public function getFechaNac() { return $this -> fechaNac; }
        public function setFechaNac(DateTime $fechaNac) { $this -> fechaNac = $fechaNac; }

        public function getDni() { return $this -> dni; }
        public function setDni(string $dni) { $this -> dni = $dni; }

        public function getDirPost() { return $this -> dirPost; }
        public function setDirPost(string $dirPost) { $this -> dirPost = $dirPost; }

        public function getDirFact() { return $this -> dirFact; }
        public function setDirFact(string $dirFact) { $this -> dirFact = $dirFact; }


      
        

    }
?>