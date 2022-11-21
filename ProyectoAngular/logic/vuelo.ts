async function GetVueloByFechaPrecio(precio: number, fechaSalida: Date, fechaLlegada: Date) {
    try {
      const response = await fetch('http://88.17.26.37:5000/vuelo', {
        method: 'POST',
        body: JSON.stringify({
          precio: precio,
          fechaSalida: fechaSalida,
          fechaLlegada: fechaLlegada,
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