export default function getStudentsByLocation(ListOfStudents, city) {
  return ListOfStudents.filter(student => student.location === city);
}
