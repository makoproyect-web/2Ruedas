import {
  pgTable,
  uuid,
  text,
  timestamp,
} from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: uuid("id").defaultRandom().primaryKey(),

  email: text("email").notNull(),

  role: text("role").notNull(),

  createdAt: timestamp("created_at")
    .defaultNow()
    .notNull(),
});