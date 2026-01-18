/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   arg_support.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 22:20:36 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/16 22:20:38 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef ARG_SUPPORT_H
# define ARG_SUPPORT_H

# include "libft/ft_printf.h"
# include "libft/libft.h"
# include "push_swap.h"
# include <stdlib.h>
# include <unistd.h>

int	ft_process_arg(char *arg, t_d_list **stack);
int	ft_proccess_arg_split(char *arg, t_d_list **stack);

#endif