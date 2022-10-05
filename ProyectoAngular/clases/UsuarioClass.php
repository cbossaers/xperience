<?php 
    class Usuario {
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

        public function getId() { return $id; }
        public function setId(int $id) { $this -> id = $id; }

        public function getNombre() { return $nombre; }
        public function setNombre(string $Nombre) { $this -> Nombre = $Nombre; }

        public function getApellidos() { return $apellidos; }
        public function setApellidos(string $Apellidos) { $this -> apellidos = $apellidos; }

        public function getContrasena() { return $contrasena; }
        public function setContrasena(string $Contrasena) { $this -> contrasena = $contrasena; }

        public function getCorreo() { return $correo; }
        public function setCorreo(string $Correo) { $this -> correo = $correo; }

        public function getTelefono() { return $telefono; }
        public function setTelefono($Telefono) { $this -> telefono = $telefono; }

        public function getFechaNac() { return $fechaNac; }
        public function setFechaNac(Date $FechaNac) { $this -> fechaNac = $fechaNac; }

        public function getDni() { return $dni; }
        public function setDni(string $Dni) { $this -> dni = $dni; }

        public function getDirPost() { return $dirPost; }
        public function setDirPost(string $DirPost) { $this -> dirPost = $dirPost; }

        public function getDirFact() { return $dirFact; }
        public function setDirFact(string $DirFact) { $this -> dirFact = $dirFact; }


      
        

    }
?>