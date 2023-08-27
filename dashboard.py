import React from 'react';
import StudentItem from './Studenttem';

const Dashboard = ({ students, markAttendance }) => {
  return (
    <div>
      <h2>Class Dashboard</h2>
      <p>Date: {new Date().toDateString()}</p>
      <ul>
        {students.map(student => (
          <StudentItem
            key={student.id}
            student={student}
            markAttendance={markAttendance}
          />
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
