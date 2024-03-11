#!/usr/bin/node
if (process.args[0] === undefined) {
  console.log("No argument");
} else {
  console.log(process.args[0]);
}
