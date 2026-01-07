interface User {
  id: number;
  name: string;
  email: string;
  age?: number;
}

const greetUser = (user: User): string => {
  return user.age ? `Welcome!\nuser#: ${user.id}\nname: ${user.name}\n${user.email}\n${user.age}` : `Welcome!\nuser #: ${user.id}\nname: ${user.name}\n${user.email}`
};

const chris: User = {
  id: 1,
  name: "Chris",
  email: "test@test.com",
  age: 35
};

console.log(greetUser(chris));