async function GetUsuarioByCorreo(correo: string) {
    try {
      const response = await fetch('http://88.17.114.199:9879/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error('Error! status: ${response.status}');
      }

      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;

    } catch (error) {
      if (error instanceof Error) {
        console.log('Error message: ', error.message);
        return error.message;
      } else {
        console.log('Unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
}
  
  async function AddUsuario(correo: string, nombre: string, apellidos: string, telefono: number, fechaNacimiento: Date) {
    try {
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
          nombre: nombre,
          apellidos: apellidos,
          telefono: telefono,
          fechaNacimiento: fechaNacimiento,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error('Error! status: ${response.status}');
      }

      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;

    } catch (error) {
      if (error instanceof Error) {
        console.log('Error message: ', error.message);
        return error.message;
      } else {
        console.log('Unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
}

  async function UpdateUsuario(correo: string, nombre: string, apellidos: string, telefono: number, fechaNacimiento: Date) {
    try {
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
          nombre: nombre,
          apellidos: apellidos,
          telefono: telefono,
          fechaNacimiento: fechaNacimiento,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error('Error! status: ${response.status}');
      }

      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;

    } catch (error) {
      if (error instanceof Error) {
        console.log('Error message: ', error.message);
        return error.message;
      } else {
        console.log('Unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
}

  async function DeleteUsuario(correo: string) {
    try {
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error('Error! status: ${response.status}');
      }

      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;

    } catch (error) {
      if (error instanceof Error) {
        console.log('Error message: ', error.message);
        return error.message;
      } else {
        console.log('Unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
}