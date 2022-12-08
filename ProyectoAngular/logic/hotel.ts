async function GetHotelById(id: string) {
    try {
      const response = await fetch('http://88.17.114.199:9879/hotel', {
        method: 'POST',
        body: JSON.stringify({
          id: id,
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