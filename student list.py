import React from 'react';
import StudentItem from './Studenttem';

function StudentList({ students, markAttendance }) {
  return (
    <ul className="student-list">
      {students.map(student => (
        <StudentItem
          key={student.id}
          student={student}
          markAttendance={markAttendance}
        />
      ))}
    </ul>
  );
}

export default StudentList;
