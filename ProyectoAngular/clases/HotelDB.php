<?php 

    function GetHotelById() {  }

    class Hotel { //no la borro por si acaso
        
        private int $id;
        private string $tipo;
        private string $chainCode;
        private string $idAmadeus;
        private string $dupeId;
        private string $nombre;
        private int $numEstrellas;
        private string $codigoCiudad;
        private float $latitud;
        private float $longitud;

        function __construct(int $id, string $tipo, string $chainCode, string $idAmadeus, string $dupeId, string $nombre, int $numEstrellas,
                            string $codigoCiudad, float $latitud, float $longitud) {
            $this -> id = $id;
            $this -> tipo = $tipo;
            $this -> chainCode = $chainCode;
            $this -> idAmadeus = $idAmadeus;
            $this -> dupeId = $dupeId;
            $this -> nombre = $nombre;
            $this -> numEstrellas = $numEstrellas;
            $this -> codigoCiudad = $codigoCiudad;
            $this -> latitud = $latitud;
            $this -> longitud = $longitud;
        }

        public function getId() { return $this -> id; }
        public function setId(int $id) { $this -> id = $id; }

        public function getTipo() { return $this -> tipo; }
        public function setTipo(string $tipo) { $this -> tipo = $tipo; }

        public function getChainCode() { return $this -> chainCode; }
        public function setChainCode(string $chainCode) { $this -> chainCode = $chainCode; }

        public function getIdAmadeus() { return $this -> idAmadeus; }
        public function setIdAmadeus(string $idAmadeus) { $this -> idAmadeus = $idAmadeus; }

        public function getDupeId() { return $this -> dupeId; }
        public function setDupeId(string $dupeId) { $this -> dupeId = $dupeId; }

        public function getNombre() { return $this -> nombre; }
        public function setNombre(string $nombre) { $this -> nombre = $nombre; }

        public function getNumEstrellas() { return $this -> numEstrellas; }
        public function setNumEstrellas(int $numEstrellas) { $this -> numEstrellas = $numEstrellas; }

        public function getCodigoCiudad() { return $this -> codigoCiudad; }
        public function setCodigoCiudad(string $codigoCiudad) { $this -> codigoCiudad = $codigoCiudad; }

        public function getLatitud() { return $this -> latitud; }
        public function setLatitud(float $latitud) { $this -> latitud = $latitud; }

        public function getLongitud() { return $this -> longitud; }
        public function setLongitud(float $longitud) { $this -> longitud = $longitud; }


      
        

    }
?>