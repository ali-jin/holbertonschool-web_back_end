/* eslint-disable */
import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const students = await readDatabase(process.argv[2]);
      response.status(200).send(`This is the list of our students\n${students}`);
    } catch (e) {
      response.status(500).send(`Cannot load the database${e}`);
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const m = request.params.major;
    if (m !== 'CS' && m !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const students = await readDatabase(process.argv[2]);
      const correctLine = students.split('\n').filter((line) => line.includes(m));
      const index = correctLine[0].indexOf('List:');
      response.status(200).send(correctLine[0].slice(index));
    } catch (e) {
      response.status(500).send('Cannot load the database');
    }
  }
}
