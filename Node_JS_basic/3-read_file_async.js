const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');
    let students = data.split('\n');
    students = students.filter((line) => line && !line.startsWith('firstname'));

    console.log(`Number of students: ${students.length}`);

    const fields = students.reduce((acc, current) => {
      const [firstname, , , field] = current.split(',');
      if (field in acc) {
        acc[field].push(firstname);
      } else {
        acc[field] = [firstname];
      }
      return acc;
    }, {});

    for (const [field, names] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(
          ', ',
        )}`,
      );
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
